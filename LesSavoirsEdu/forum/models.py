from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

# Create your models here.
        
class Post(models.Model):
    title = models.CharField(max_length=250, null=False)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="posts")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Updates whenever saved

    def was_edited(self):
        return self.created_at != self.updated_at  # Check if edited

    def __str__(self):
        return f"Comment by {self.user} on {self.post.title}"


