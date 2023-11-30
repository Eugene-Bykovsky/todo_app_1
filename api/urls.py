from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, SubTaskViewSet

from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

app_name = 'api'

router = DefaultRouter()

router.register(r'v1/tasks', TaskViewSet)
router.register(r'v1/subtasks', SubTaskViewSet)

docs_urlpatterns = [
    path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "v1/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger-ui",
    ),
    path(
        "v1/schema/redoc/",
        SpectacularRedocView.as_view(url_name="api:schema"),
        name="redoc",
    ),
]

urlpatterns = router.urls + docs_urlpatterns
