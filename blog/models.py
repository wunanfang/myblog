from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    # 自定义get_absolute_url方法，记得从Django.urls中导入reverse函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})


