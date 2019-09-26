import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from post.models import Post
from .import forms

# Use to disply breif introduction about blog.
def about(request):
    return render(request, 'about.html') 

# Use to list all the post on home page. 
def home(request):
    posts = Post.objects.all().order_by('created_on')
    # pagination
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'posts': posts})
  
# Use to create new post.  
def create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            # save post in db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.PostForm()
        return render(request, 'create.html', {'form':form}) 

# Use to show particular post.  
def show(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'show.html', {'post':post}) 

# Use to edit particular post. 
@login_required(login_url="/accounts/login/")
def edit(request, pk):
    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            form = forms.PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                # save edited post in db.
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('home')
        else:
            form = forms.PostForm(instance=post)
        return render(request, 'edit.html', {'form': form})
    else:
        return redirect('home')

# Use to delete particular post. 
@login_required(login_url="/accounts/login/")
def delete(request, pk):
    if request.user.is_superuser:
        post = Post.objects.get(pk=pk)
        if post.delete():
            return redirect('home')
        else:
            return render(request, 'show.html', {'post': post})
    else:
        return redirect('home')

# Use to download post.
@login_required(login_url="/accounts/login/")
def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    writer.writerow(['Id', 'Title', 'Slug', 'Content', 'Created_on', 'Image', 'Author'])
    posts = Post.objects.all()
    for post in posts:
        writer.writerow([post.id, post.title, post.slug, post.content, post.created_on, post.image, post.author])
    return response


