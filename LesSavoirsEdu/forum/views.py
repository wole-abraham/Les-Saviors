from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from courses.models import Course
from forum.models import Comment

# Create your views here.

@login_required
def forum(request):
    if request.method == "POST":
        author = request.user
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get('post_image')
        course = Course.objects.filter(title=request.POST.get("course")).first()

        Post.objects.create(author=author,
                            title=title,
                            content=content,
                            image = image,
                            course=course)
        return redirect(forum)
    return render(request, 'forum/forum.html', {'posts': Post.objects.all().order_by('-id'), 'courses': Course.objects.all()})

@login_required
def Post_comment(request, post_id):
    if request.method == "POST":
        content = request.POST.get("comment")
        user = request.user
        comment = Comment()
        comment.post = Post.objects.filter(id=post_id).first()
        comment.user = user
        comment.content = content
        comment.save()
        return redirect(forum)
    return redirect(forum)

