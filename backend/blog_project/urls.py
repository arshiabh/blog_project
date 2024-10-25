"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from users import views as register_view
from django.contrib.auth import views as auth_views
#in2ta paeen vase setting image
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("blog.urls")),
    path("register/", register_view.register, name="register"),
    path("profile", register_view.profile, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", register_view.log_out, name="logout"),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    #2ta variable to url zir khode template django mikhad
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset/done", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)