from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInfo(models.Model):
    user =  models.OneToOneField(User)
    pic = models.ImageField(blank = True, upload_to='pics')
    my_link  = models.URLField(blank  = True)

    def __str__(self):
        return self.user.username
# Create your models here.
