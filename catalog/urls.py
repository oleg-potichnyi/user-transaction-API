from django.urls import path, include
from rest_framework import routers
from catalog.views import UserViewSet, TransactionViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("transactions", TransactionViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "catalog"
