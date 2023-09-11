from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post, Comments
from blog.forms import PostForm

def post_list(request):
    posts = Post.objects.all().filter(status_published_post=True)
    context = {'items': posts}
    return render(request, 'blog/post_list.html', context)

def post_status(request):
    #Функция отвечающая за добавление поста в режим "неопубликованные"
    posts = Post.objects.all().filter(status_published_post=False)
    context = {'items': posts}
    return render(request, 'blog/post_list.html', context)

def published_post(request, post_pk):
    #Функция которая отвечает за выход поста из "неопубликованные" в "опубликованные"
    post = Post.objects.get(pk=post_pk)
    post.status_published_post = True
    post.save()
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)




def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = Comments.objects.filter(post=post_pk)
    kol_comments = comments.count()
    return render(request, 'blog/post_detail.html', {
                                                    'post': post,
                                                     'comments': comments,
                                                     'kol_comments': kol_comments
                                                                        })

def post_new(request):
    if request.method == 'GET':
        form = PostForm
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = PostForm(request.POST, instance=post )
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)


def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk).delete()
    return redirect('post_list')
