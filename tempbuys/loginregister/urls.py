from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path('logout', views.logout, name='logout'),
    path("bill", views.bill, name="bill"),
    path("forgot_password",views.forgot_password,name='forgot_password'),
    path("is_otp_expired",views.is_otp_expired,name="is_otp_expired"),
    path("handle_otp",views.handle_otp,name="handle_otp"),
    path("password_update",views.password_update,name="password_update"),
    path("profile_page", views.profile_page, name="profile_page"),
    path("profile_password", views.profile_password, name="profile_password"),
    path("profile_forgot_password", views.profile_forgot_password, name='profile_forgot_password'),
    path("profile_handle_otp", views.profile_handle_otp, name="profile_handle_otp"),
    path("profile_password_update", views.profile_password_update, name="profile_password_update"),
    path('verify_email/<str:token>/', views.verify_email, name='verify_email'),


]