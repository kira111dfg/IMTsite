from django.urls import path,include
from . import views
from users.views import Register

app_name='users'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('register/',Register.as_view(),name='register'),
    path('profile/<int:user_pk>', views.ProfileView.as_view(), name='profile'),
    path('profile_update/', views.profile, name='profile_update'),

]