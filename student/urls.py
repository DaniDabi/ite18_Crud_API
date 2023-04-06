from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path ('', views.login_user, name="login"),
    path('show',views.show, name= "show"),
    path('emp', views.emp),    
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
]  