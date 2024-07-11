
from django.urls import path
from .views import *
urlpatterns = [
    path("emp/",ToDoDetail.as_view(), name="emp"),
    path("emp/<int:id>/", ToDoInfo.as_view())
]

