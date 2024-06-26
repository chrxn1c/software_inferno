from django.urls import path

from .views import SoftwareViewSet

urlpatterns = [
    path('software', SoftwareViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('software/<str:software_name>', SoftwareViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
    ))
]
