from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User

# Create your models here.
class postmodel(models.Model):
    post_title = models.CharField(max_length=50, null = False)
    post_summary = models.TextField()
    post_body = tinymce_models.HTMLField()
    post_image = models.ImageField(upload_to = 'post_media/', null = True) 

    def __str__(self) -> str:
        return self.post_title 

class commentmodel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(postmodel, on_delete=models.CASCADE)
    comment_body=models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_body

class contactmodel(models.Model):
    Name = models.CharField(max_length=32, null=False)
    Email = models.CharField(max_length=32, null=False)
    Mobile_Number = models.CharField(max_length=12)
    Query = models.TextField(max_length=320, null=False)
    Added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.Name
