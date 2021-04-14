from django.urls import path
from django.views.generic import TemplateView
from .views import PostListView

urlpatterns = [
    path('', TemplateView.as_view(template_name = "index.html")),
    path('posts',PostListView.as_view()),
]