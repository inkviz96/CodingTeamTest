from django.urls import path
from testjob.views import get_food

urlpatterns = [
    path('foods/', get_food),
]
