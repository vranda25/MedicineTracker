from django.urls import path
from .views import *
# from myapi.core import views

urlpatterns = [
    path('', ProfileView.as_view()),
    path('allergy/', AllergiesView.as_view()),
    path('history/', HistoryView.as_view()),
]