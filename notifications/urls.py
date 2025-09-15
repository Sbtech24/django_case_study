from django.contrib import admin
from django.urls import path
from notifications.views import send_email_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("send-email/", send_email_view),  
]
