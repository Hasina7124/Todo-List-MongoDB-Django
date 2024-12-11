from django.urls import path
from .views import*

app_name = "todolist"
urlpatterns = [
    path("create", create, name='create'),
    path("", read, name='read'),
    path("delete", delete, name='delete'),
    path("update", update, name='update'),
    path("modify", modify, name='modify'),
    path("achever", achever, name='achever'),
]