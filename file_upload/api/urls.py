from django.urls import path

from .views import FileListView, FileUploadView

app_name = 'api'


urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='upload'),
    path('files/', FileListView.as_view(), name='files')
]
