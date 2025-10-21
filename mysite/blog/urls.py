from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),           # 글 목록
    path('new/', views.post_new, name='post_new'),         # 새 글 작성
    path('<int:pk>/', views.post_detail, name='post_detail'), # 글 상세 보기
    path('<int:pk>/edit/', views.post_edit, name='post_edit'), # 글 수정
    path('<int:pk>/delete/', views.post_delete, name='post_delete'), # 글 삭제
]
