from django.urls import path

from storage.views import UploadViewSet

upload_detail = UploadViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})
upload_create = UploadViewSet.as_view({
    'post': 'create'
})
urlpatterns = [
    path('', upload_create, name='upload-create'),
    path('<str:hash>/', upload_detail, name='upload-detail'),

]
