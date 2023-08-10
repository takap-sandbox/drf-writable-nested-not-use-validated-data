from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookAPIViewSet

app_name = "api"
router = DefaultRouter()
router.register("books", BookAPIViewSet, basename="books")

urlpatterns = [
    path("", include(router.urls))
]
