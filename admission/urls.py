"""admission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_login_reg import views as user_views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verifier_home/', user_views.verifier_home, name='verifier-home'),
    path('', user_views.main, name='home-page'),
    path('register/', user_views.register, name='register'),
    path('register/otp/', user_views.otp, name='verification'),
    path('logi/',  user_views.logi, name='logi'),
    path('logo/', user_views.logo, name='logo'),
    path('adm/',user_views.adm,name='adm'),
    path('seat/',user_views.seat,name='seat'),
    path('v_register/', user_views.v_register),
    path('register/payment/', user_views.payment),
    path('login/', user_views.login, name='login'),
    path('login/applicant_login/', user_views.applicant_login, name='applicant-login'),
    path('login/verifier_login/', user_views.verifier_login, name='verifier-login'),
    # path('login/student_login/password_reset/', user_views.),
    # path('login/verifier_login/password_reset/', user_views.),
    path('applicant_home/', user_views.applicant_home, name='applicant-home'),
    path('applicant_home/display/', user_views.display, name='display'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_login_reg/logout.html'), name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='user_login_reg/password_reset_form.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='user_login_reg/password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='user_login_reg/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user_login_reg/password_reset_complete.html'),name='password_reset_complete'),
    path('verify_Verify/',user_views.verifier_Verify,name="verifier-verify"),
]

#    href="{% url YOUR_VIEW column_3_item.pk %}/?next={{column_3_item.link_for_item|urlencode:''}}"