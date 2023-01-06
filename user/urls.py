from django.urls import path

from user import views

urlpatterns = [
    path('', views.UserDetail.as_view(), name='user_detail'),
    path('password/', views.UserPassword.as_view(), name='user_change_password'),
    path('signup/', views.SignupUser.as_view(), name='signup'),
    path('verify/phone/', views.VerifyUserPhone.as_view(), name='verify_phone'),
    path('verify/email/', views.VerifyUserPhone.as_view(), name='verify_email'),
    path('signin/', views.SigninUser.as_view(), name='signin'),
    path('resend/phone/', views.ResendPhoneCode.as_view(), name='resend_phone_code'),
    path('resend/email/', views.ResendEmailCode.as_view(), name='resend_email_code'),
]
