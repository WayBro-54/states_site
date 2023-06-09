from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=124,
                             unique=True,
                             verbose_name='Заголовок')
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,
                             related_name='post',
                             on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

    # images = models.ImageField(upload_to='media')
    