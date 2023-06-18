from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm

def forums(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'forum_app/forums.html', context)

@login_required
def createPost(request):

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.user
            title = request.POST['title']
            description = request.POST['description']

            Post.objects.create(
                user = user,
                title = title,
                description = description,
            )

            return redirect('forums')

    context = {'form': form}
    return render(request, 'forum_app/post-form.html', context)

def post(request, pk):

    post = Post.objects.get(id=pk)
    comments = post.comment_set.all()

    if request.method == 'POST':
        user = request.user
        message = request.POST['message']

        Comment.objects.create(
            user = user,
            post = post,
            message = message
        )

        return redirect('post', pk=post.id)

    context = {'post': post, 'comments': comments}
    return render(request, 'forum_app/post.html', context)
