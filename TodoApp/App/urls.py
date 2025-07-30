from django.urls import path
from . import views 
urlpatterns = [
    path('',views.homepage,name="homepage"), 
    path('edit/<int:pk>',views.edit,name="edit"),
    path('login/',views.loginpage,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.userlogout,name="logout"),
    path('addtodo/',views.addtodo,name="addtodo"),
    path('profileedit/<int:pk>',views.profileedit,name="profileedit"),
    path('edittodo/<int:pk>',views.edittodo,name="edittodo"),
    path('todocomplete/<int:pk>',views.todocomplete,name="todocomplete"),
    path('trash/<int:pk>',views.trash,name="trash"),
    path('tododelete/<int:pk>',views.tododelete,name="tododelete"),
] 