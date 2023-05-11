from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('' , Home , name="Home"),
    path('register' , register_page ,name="register_page"),
    path('login', login_page, name="login_page"),
    # path('my-notes' , my_notes , name="my_notes"),
    path('edit/<uuid:id>', NotesEdit , name="NotesEdit"),  
    path('update/<uuid:id>', Notesupdate , name="Notesupdate"),  
    path('delete_product/<uuid:id>', delete,name="delete"), 
    path('logout', Logout, name="Logout"),



    

]
