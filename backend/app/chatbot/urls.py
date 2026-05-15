from django.urls import path
from .views import ChatbotAnswerView

urlpatterns = [
    path('get-answer/', ChatbotAnswerView.as_view(), name='get-answer'),
]
