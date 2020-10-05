"""calendar_server URL Configuration

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
from calendar_server.views.schedules.views import SchedulesViews, ScheduleViews
from calendar_server.views.tags.views import TagsViews, TagViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # apis
    path('api/v1/schedules/', SchedulesViews.as_view(), name='schedules'),
    path('api/v1/schedule/', ScheduleViews.as_view(), name='schedule'),
    path('api/v1/tags/', TagsViews.as_view(), name='tags'),
    path('api/v1/tag/', TagViews.as_view(), name='tag'),
]
