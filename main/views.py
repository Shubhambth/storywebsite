from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from .models import Post
from .models import Comment
from .forms import CommentForm

def home(request):
    query = request.GET.get('q')  # Get the search query
    if query:
        posts = Post.objects.filter(title__icontains=query)  # Search posts by title
    else:
        posts = Post.objects.all().order_by('-created_at')
    popular_posts = Post.objects.order_by('-views')[:5]
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
        'popular_posts': popular_posts,
        'categories': categories,
        'query': query,
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.views += 1  # Increment views count
    post.save()

    # Handle comments
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        form = CommentForm()

    comments = post.comments.all()  # Fetch comments related to the post
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    return render(request, 'category_posts.html', {
        'category': category,
        'posts': posts,
    })


