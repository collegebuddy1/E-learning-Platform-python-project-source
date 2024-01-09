"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic.base import TemplateView  # new
from elearning.views import about_view, session_view, class_view,lecturer_view,lecturers_view,user_edit_view,passwordschangeview,password_success,user_register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # new
    path("about/", about_view, name="about"),
    path("session/", session_view, name="session"),
    path("class/<int:my_id>/", class_view, name="class"),
    path("lecturers/", lecturers_view, name="lecturers"),
    path("lecturer/<int:my_id>/",lecturer_view , name="lecturer"),
    path('tinymce/', include('tinymce.urls')),
    path("profile/",user_edit_view.as_view() , name="profile"),
    path("password/",passwordschangeview.as_view(template_name="registration/change-password.html"),name="password"),
    path("password_success",password_success,name="password_success"),
    path("register/",user_register_view.as_view(),name="register"),




]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)