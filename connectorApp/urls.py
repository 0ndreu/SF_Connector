from django.urls import path, include
from .views import VacancyList

urlpatterns = [
    path('', VacancyList.as_view()),
]
