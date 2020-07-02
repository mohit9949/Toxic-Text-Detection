from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('api',views.APiViewSet)
urlpatterns = [
path('api_service/',include(router.urls)),
path('status/',views.predict),
]
