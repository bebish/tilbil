from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Category, Topic, Post

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'forum/category_list.html', {'categories': categories})

def topic_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = category.topics.all()
    return render(request, 'forum/topic_list.html', {'category': category, 'topics': topics})

def post_list(request, category_id, topic_id):
    topic = get_object_or_404(Topic, id=topic_id, category_id=category_id)
    category = get_object_or_404(Category, id=category_id)
    posts = topic.posts.all()
    topics = category.topics.all()
    return render(request, 'forum/post_list.html', {'topic': topic, 'posts': posts, 'category': category, 'topics': topics})

@login_required
def create_topic(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        title = request.POST['title']
        topic = Topic.objects.create(
            title=title,
            category=category,
            created_by=request.user
        )
        return redirect('post_list', category_id=category.id, topic_id=topic.id)
    return render(request, 'forum/create_topic.html', {'category': category})

@login_required
def create_post(request, category_id, topic_id):
    topic = get_object_or_404(Topic, id=topic_id, category_id=category_id)
    if request.method == 'POST':
        message = request.POST['message']
        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=request.user
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def load_topics(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = category.topics.all()
    html = render_to_string('forum/topic_list.html', {'category': category, 'topics': topics}, request=request)
    return JsonResponse({'html': html})

def load_chat(request, category_id, topic_id):
    topic = get_object_or_404(Topic, id=topic_id, category_id=category_id)
    posts = topic.posts.all()
    html = render_to_string('forum/post_list.html', {'topic': topic, 'posts': posts}, request=request)
    return JsonResponse({'html': html})
