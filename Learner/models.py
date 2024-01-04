from django.db import models

# Create your models here.
class Learner(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 255)
    profile_pic = models.FileField(upload_to = 'user_pics', default='default.jpg')
    mobile = models.CharField(max_length = 255)

    def __str__(self):
        return self.email