"""my_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('todo/', index)
    # path('', views.homepage, name='homepage'),
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('passwordreset', views.passwordreset, name='passwordreset'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('task_detail/<int:tid>', views.task_detail, name='task_detail'),
    path('task_edit/<int:tid>', views.task_edit, name='task_edit'),
    path('task_delete/<int:tid>', views.task_delete, name='task_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
