
from django.urls import path
from . import views
urlpatterns =[
    path('',views.login,name="login"),
    path('register',views.register,name="register"),

    path('home',views.home,name="home"),
    path('display',views.display,name="display"),
    path('discard/<str:bookId>',views.discard),
    path('edit/<str:bookId>',views.edit),
    path('update/<str:bookId>',views.update),
    path('show',views.show,name="show")
    
    
]
    