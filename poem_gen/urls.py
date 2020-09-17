from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from poem_gen import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(
        template_name='poem_gen/login.html'), name='login'),
    path('logout/', LogoutView.as_view(
        next_page='index'), name='logout'),
    path('view-notebook/', views.view_notebook, name='view-nb'),
    path('write-line/', views.write_line, name='write-line'),
    path('get-poem/', views.get_poem, name='get-poem'),
]

