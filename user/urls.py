from django.urls import path

from user import views

urlpatterns = [
    # path('/'),
    path('signup/', views.SignupUser.as_view(), name='signup'),
    path('verify/', views.VerifyUserPhone.as_view(), name='verify'),
    path('signin/', views.SigninUser.as_view(), name='signin'),
    path('resend/phone/', views.ResendPhoneCode.as_view(), name='resend_phone_code'),
    path('resend/email/', views.ResendEmailCode.as_view(), name='resend_email_code'),
]
