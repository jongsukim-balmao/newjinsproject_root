from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

def health(_):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
]
