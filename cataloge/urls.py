from django.urls import path,include, reverse_lazy    
from .import views
from django.contrib.auth import views as auth_v

urlpatterns = [
    path('',views.index,name='index'),      
    path('create_book',views.BookCreate.as_view(),name='create_book'),      
    path('detail_book/<int:pk>',views.BookDetail.as_view(),name='detail_book'),      
    path('accounts/register',views.Register.as_view(),name='register'),      
    path('accounts/pass_change',auth_v.PasswordChangeView.as_view(template_name='registration/pass_change.html',success_url = reverse_lazy('login')),name='pass_change'),      
]