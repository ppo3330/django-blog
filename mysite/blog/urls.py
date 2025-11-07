from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),           # 글 목록
    path('new/', views.post_new, name='post_new'),         # 새 글 작성
    path('<int:pk>/', views.post_detail, name='post_detail'), # 글 상세 보기
    path('<int:pk>/edit/', views.post_edit, name='post_edit'), # 글 수정
    path('<int:pk>/delete/', views.post_delete, name='post_delete'), # 글 삭제
    path('<int:post_pk>/comment/<int:comment_pk>/edit/', views.comment_edit, name='comment_edit'), #댓글 수정
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'), #댓글 삭제

]
