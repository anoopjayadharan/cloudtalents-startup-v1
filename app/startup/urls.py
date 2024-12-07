from django.urls import path
from .views import home, register, UserLoginView, upload_image, image_list, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='user_logout'),
    path('upload/', upload_image, name='upload_image'),
    path('images/', image_list, name='image_list'),
]
