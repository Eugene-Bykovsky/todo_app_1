from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, SubTaskViewSet

app_name = 'api'

router = DefaultRouter()

router.register(r'tasks', TaskViewSet)
router.register(r'subtasks', SubTaskViewSet)

urlpatterns = (
    path('', include(router.urls)),
)
