from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post, Comments, Category, Feedback
from blog.forms import PostForm, CommentForm
from django.db.models import Avg

def raiting(post_pk):
    '''
    рейтинг отзыва на посты
    '''
    fb = Feedback.objects.filter(post=post_pk)
    count = sum([i.raiting for i in fb]) / fb.count()  # Делит общию оценку рейтинга на общее количество
    return round(count, 1) #Ограничение на количество отзывов


def post_raiting(request):
    '''
    Фильтрация постов по рейтингу на главной странице
    '''
    posts = Post.objects.values('title', 'pk').annotate(Avg('feedbacks__raiting')).order_by('feedbacks__railing__avg')
    return render(request, 'blog/post_list.html', {
                                                                        'items': posts,
                                                                        })


def post_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)
    else:
        posts = Post.objects.all().filter(status_published_post=True)


    category = Category.objects.all()

    context = {'items': posts,
               'category': category
               }
    return render(request, 'blog/post_list.html', context)

def categories(request, category_pk):
    posts = Post.objects.filter(category=category_pk)
    category = Category.objects.all()
    context = {'items': posts,
               'category': category
               }
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
    raiting_count = raiting(post_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.published_date = datetime.now()
            comment.save()
            return redirect('post_detail', post_pk=post_pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
                                                     'post'         : post,
                                                     'comments'     : comments,
                                                     'kol_comments' : kol_comments,
                                                     'comment_form' : comment_form,
                                                     'raiting': raiting_count
                                                                        })

def post_new(request):
    if request.method == 'GET':
        form = PostForm
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST, request.FILES)
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
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)

def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk).delete()
    return redirect('post_list')


def feedback(request, post_pk):
    '''
    Функция для вызова отзывов
    '''
    post = Post.objects.get(pk=post_pk)
    fb = Feedback.objects.filter(post=post_pk)


    context = {
        "fb": fb,
        "post": post,

    }
    return render(request, 'blog/feedback.html', context)




