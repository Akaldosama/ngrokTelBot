from django.urls import path
from .views import num_to_words

urlpatterns = [
    path('convert/', num_to_words, name='num_to_words'),
]
