from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    cover = models.ImageField(upload_to='images/')
    body = models.TextField()

    class Meta:
        ordering = ['-id', ]
 
    def __str__(self):
        return self.title