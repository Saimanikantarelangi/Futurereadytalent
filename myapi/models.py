from django.db import models
from django.utils import timezone



class User(models.Model):
        Username = models.CharField(max_length=40)
        email = models.CharField(max_length=50, unique=True)
        phone = models.CharField(max_length=30)
        pass1 = models.CharField(max_length=200)

        def __str__(self):
            return self.Username

class Posts(models.Model):
    aurt = models.CharField(max_length=15,default=User)
    title = models.CharField(max_length=20)
    content = models.TextField()
    date = models.DateTimeField(blank=True,default=timezone.now)
    Username = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)

    class Meta:
        verbose_name_plural="Posts"

    class Meta:
        ordering = ['-date', ]

    def __str__(self):
        return self.title+ ' by ' +self.aurt
