from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def post_list(request):
    query = request.GET.get('q')
    if query:   #제목이나 내용에 검색어가 포함된 글만 검색
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    else:   #검색어가 없을 때는 전체 글
        posts = Post.objects.all()
        
    posts = posts.order_by('-created_at')    #항상 최신 글이 위로 오게 정렬

    paginator = Paginator(posts, 5)             #페이지네이션 추가 (한 페이지에 5개씩)
    page_number = request.GET.get('page')       #항상 최신 글이 위로 오게 정렬
    page_obj = paginator.get_page(page_number)  # 해당 페이지에 해당하는 글만 가져오기

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'query': query
        })

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
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)    #삭제할 글을 DB에서 찾기
    if request.method == "POST":             #진짜 삭제 버튼이 눌린 경우
        post.delete()                        #DB에서 삭제 실행
        return redirect('post_list')         #삭제 후 글 목록 페이지로 이동
    return render(request, 'blog/post_delete.html', {'post': post})  #삭제 확인 페이지 보여주기
