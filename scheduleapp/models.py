from django.db import models

   
class Post(models.Model):
    title = models.CharField(verbose_name='title', max_length=200)
    naiyo = models.TextField(verbose_name='naiyo', )
    syosai = models.TextField(verbose_name='syosai', )
    
    def __str__(self):
        return self.title
