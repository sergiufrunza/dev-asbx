from django.urls import path
from .api_v1 import *
urlpatterns = [
    path('api/v1/sendemail/', SendEmailAPI.as_view()),
    path('api/v1/sendemaildocusign/', SendEmailDocuSignAPI.as_view()),
]