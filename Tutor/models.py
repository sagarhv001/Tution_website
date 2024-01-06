from django.db import models


# Create your models here.


class Technology(models.Model):
    technology = models.CharField(max_length=255)

    def __str__(self):
        return self.technology

class Tutor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    technology = models.ManyToManyField(Technology)
    experience = models.CharField(max_length=255)
    profile_pic = models.FileField(upload_to='tutor_pics', default='default.jpg')
    mobile = models.CharField(max_length=255)
    
    def __str__(self):
        return self.first_name

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_description = models.TextField()
    course_duration = models.CharField(max_length=255)
    Tutor=models.ForeignKey(Tutor, on_delete=models.CASCADE)
    technology=models.ManyToManyField(Technology)
    course_file = models.FileField(upload_to='course')

    def __str__(self):
        return self.course_name

    

