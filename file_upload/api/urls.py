from django.urls import path

from .views import FileListView, FileUploadView

app_name = 'api'


urlpatterns = [
    path('file_upload/', FileUploadView.as_view(), name='file_upload'),
    path('files/', FileListView.as_view(), name='files')
]
