from django.db import models
from tinymce.models import HTMLField


class BlogPost(models.Model):
    """
    Here we'll define our Post model
    """

    # author is linked to a registered
    # user in the 'auth_user' table.
    slug = models.SlugField(max_length=50, default="none" )
    blog_name = models.CharField(max_length=200)
    blog_content = HTMLField(default="-")
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.blog_name

# Create your models here.
