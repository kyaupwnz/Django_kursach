from django.urls import path

from blog.apps import BlogConfig
from blog.views import RecordListView, RecordCreateView, RecordUpdateView, RecordDeleteView, RecordDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('', RecordListView.as_view(), name='record_list'),
    path('create_record/', RecordCreateView.as_view(), name='create_record'),
    path('update/<slug:slug>/', RecordUpdateView.as_view(), name='update_record'),
    path('delete/<slug:slug>/', RecordDeleteView.as_view(), name='delete_record'),
    path('detail/<slug:slug>/', RecordDetailView.as_view(), name='record_detail')
]
