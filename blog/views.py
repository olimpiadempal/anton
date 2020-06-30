from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.db.models import Q






def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog/post_list.html', {'posts': posts})
    
    category = request.GET.get('category')
    if category:
        posts = posts.filter(category=category)
    return render(request, 'blog/post_list.html', {'posts': posts, 'category_choices': Post.CATEGORY_CHOICES })








    paginator = Paginator(queryset_list, 10)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)


def post_detail(request, pk):
    Post.objects.get(pk=pk)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
       
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        
    return render(request, 'blog/post_edit.html', {'form': form})




