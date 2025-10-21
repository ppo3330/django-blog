from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # 글 목록 페이지로 이동
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)      # ① 수정할 글을 DB에서 불러오기. 없으면 404 에러
    if request.method == "POST":               # ② 수정 폼이 제출된 경우
        form = PostForm(request.POST, instance=post)  # ③ 기존 글을 폼에 연결
        if form.is_valid():                    # ④ 입력값이 유효하면
            form.save()                        # ⑤ DB에 저장 (수정된 내용 반영)
            return redirect('post_detail', pk=post.pk)  # ⑥ 수정 후 상세 페이지로 이동
    else:
        form = PostForm(instance=post)         # ⑦ 처음 열었을 때 기존 내용이 담긴 폼을 보여줌
    return render(request, 'blog/post_edit.html', {'form': form})  # ⑧ 템플릿에 폼 전달

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)    # ① 삭제할 글을 DB에서 찾기
    if request.method == "POST":             # ② 진짜 삭제 버튼이 눌린 경우
        post.delete()                        # ③ DB에서 삭제 실행
        return redirect('post_list')         # ④ 삭제 후 글 목록 페이지로 이동
    return render(request, 'blog/post_confirm_delete.html', {'post': post})  # ⑤ 삭제 확인 페이지 보여주기
