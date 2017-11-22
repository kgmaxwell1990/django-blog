from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, BlogCommentForm
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your views here.
def blogposts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})
    
    
def viewpost(request, slug):
    this_post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=this_post)
    form = BlogCommentForm()
    return render(request, "viewpost.html", {'post': this_post, 'comments': comments, 'form': form})


@login_required()
def newpost(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect(viewpost, post.slug)
    else:
        form = BlogPostForm()
    return render(request, 'postform.html', {'form': form})
    
    
def editpost(request, slug):
   post = get_object_or_404(Post, slug=slug)
   
   if request.method == "POST":
       form = BlogPostForm(request.POST, request.FILES, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.slug = slugify(post.title)
           post.author = request.user
           post.created_date = timezone.now()
           post.published_date = timezone.now()
           post.save()
           return redirect(viewpost, post.slug)
   else:
       form = BlogPostForm(instance=post)
   return render(request, 'postform.html', {'form': form, 'post': post})
   
def deletepost(request, slug):
     post = get_object_or_404(Post, slug=slug)
     post.delete()
     return redirect('home')
     
     
def addcomment(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    form = BlogCommentForm(request.POST)  
    if form.is_valid():
        comment = form.save(commit=False)

        comment.author = request.user
        comment.post = post

        comment.save()        
        return redirect('viewpost', post_id)
    
    
    
    