from django.urls import path
from Verification.Api.api_v1 import *
urlpatterns = [
    path('api/v1/sendverificationcode/', SendVerificationCode.as_view()),
    path('api/v1/checkverificationcode/', CheckVerificationCode.as_view()),
]