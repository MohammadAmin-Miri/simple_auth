from django.urls import path

from user import views

urlpatterns = [
    # path('/'),
    path('signup/', views.SignupUser.as_view(), name='signup'),
    # path('verify/',),
    # path('signin/',),
    # path('resend/',),
]
