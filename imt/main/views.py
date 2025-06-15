
from django.urls import reverse, reverse_lazy

from users.models import Profile
from .forms import CountForm, PostForm, DietForm
from .models import IMT, Dish,Category,Dietary, catDietary
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView,ListView,CreateView
from itertools import chain
from django.contrib.auth.models import User


class Search(ListView):
    template_name='main/search.html'
    context_object_name='dishes'


    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        dishes = Dish.objects.filter(title__icontains=query)
        menu = Dietary.objects.filter(title__icontains=query)
        
        results = chain(menu,dishes)
        return results
    

    


def HomeView(request):
    return render(request,'main/home.html')
   
    

def ImtPage(request):
    i=IMT.objects.latest('time_create')
    menu=Dietary.objects.all().order_by('-id')
    highs=Dietary.objects.all().filter(cat__name='high').order_by('-id')[:3]
    midls=Dietary.objects.all().filter(cat__name='midl').order_by('-id')[:3]
    lows=Dietary.objects.all().filter(cat__name='low').order_by('-id')[:3]
    return render(request,'main\imt.html',{'i':i,'menu':menu,'lows':lows,'midls':midls,'highs':highs})



def CounterView(request):
    if request.method=='POST':
        form=CountForm(request.POST)
        if form.is_valid():
            f=IMT(
                weight=form.cleaned_data['weight'],
                height=form.cleaned_data['height'],
            )
            f.save()
            return redirect('imtPage')
        else:
            form.add_error(None, 'Ошибка добавления поста')
    form=CountForm()

    imts=IMT.objects.all()
    return render(request,'main\counter.html',{'imts':imts,'form':form})


class ShowDishList(ListView):
    model = Dish
    template_name = 'main/dish_list.html'
    context_object_name = 'dishes'



class CategoryView(ListView):
    model = Dish
    template_name = 'main/category.html'
    context_object_name = 'dish_category'


    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Dish.objects.all().filter(cat__slug=self.category.slug)
        return queryset
    

class ShowPost(DetailView):
    model=Dish
    template_name='main/dish.html'
    context_object_name = 'post'
    

class DietaryList(ListView):
    model = Dietary
    template_name = 'main/dietary_list.html'
    context_object_name = 'dietaries'
    paginate_by=3

class ShowDiet(DetailView):
    model=Dietary
    template_name='main/diet.html'
    context_object_name = 'diet'




class CategoryView1(ListView):
    model = Dietary
    template_name = 'main/category1.html'
    context_object_name = 'diet_category'
    category=None
    paginate_by=3


    def get_queryset(self):
        self.category = catDietary.objects.get(slug=self.kwargs['slug'])
        queryset = Dietary.objects.all().filter(cat__slug=self.category.slug)
        return queryset



class AddPost(CreateView):
    form_class = PostForm
    template_name = 'main/addpost.html'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class AddDiet(CreateView):
    form_class = DietForm
    template_name = 'main/adddiet.html'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

class Post(ListView):
    model=Dish
    context_object_name='dishes'
    template_name='main/post_list'

    def get_queryset(self):
        return Dish.objects.filter(author_id=self.kwargs['user_id'])
    
class Menu(ListView):
    model=Dietary
    context_object_name='dietaries'
    

    def get_queryset(self):
        return Dietary.objects.filter(author_id=self.kwargs['user_id'])