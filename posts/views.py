from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.core.files.storage import FileSystemStorage

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        myfile = request.FILES['image']
        fs = FileSystemStorage('post_images')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})