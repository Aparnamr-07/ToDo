from django.urls import path
from . import views 
urlpatterns = [
    path('',views.homepage,name="homepage"), 
    path('task/',views.task,name="task"),
    path('edit/',views.edit,name="edit"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.userlogout,name="logout"),
    
]