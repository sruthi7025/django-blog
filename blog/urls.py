from django.urls import path
from.import views

urlpatterns=[
    path("",views.index,name="index",),
    path('post/<int:id>/', views.post, name='post'),
    path("create",views.create,name='create'),
    path("register",views.register,name='register'),
    path("contact",views.contact,name='contact'),
    path("about",views.about,name='about'),
    path("edit/<int:id>/",views.edit,name="edit"),
    path("delete/<int:id>/",views.delete,name="delete")
]