from django.urls import path
from .views import PostList, PostDetail
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),

]