from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 30,unique = True)
    description = models.CharField(max_length = 100)
    is_done = models.BooleanField(verbose_name = 'is_done',default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')

    def __str__(self):
        return self.title
