from django.urls import path

from file.apps import FileConfig
from file.views.drf_views import FileUploadAPIView, FileListAPIView
from file.views.views import home, FileListView, FileDetailView, FileDeleteView, DownloadFileView

app_name = FileConfig.name

urlpatterns = [
    path('', home, name='home'),  # http://127.0.0.1:8000/
    path('all/', FileListView.as_view(), name='all_files'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    path('file/download/<int:pk>/', DownloadFileView.as_view(), name='file_download'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),

    #
    path('upload_file/', FileUploadAPIView.as_view(), name='upload_file'),
    path('all_files/', FileListAPIView.as_view(), name='all-files'),
]
