from django.urls import path
from .views import *


urlpatterns = [
    path('', ProfileView.as_view()),
    path('allergy/', AllergiesView.as_view()),
    path('history/', HistoryView.as_view()),
]