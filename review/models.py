from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Profile(models.Model):
    fullname = models.CharField(null=True,max_length=50)
    user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE,null=True, blank=True)
    bio=models.TextField(null=True,max_length=200)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images',null=True, blank=True)
    contacts = models.CharField(null=True,max_length=15)
    def save_profile(self):
        self.save()
    
    def delete_profile(self): 
        self.delete()

    def __str__(self):
        return(self.fullname)

class Projects(models.Model):
    landing_page = models.ImageField(default='default.jpg', upload_to='images',null=True, blank=True)
    description = models.TextField(null=True,max_length=200)
    title = models.CharField(null=True,max_length=200)
    link = models.URLField(null=True,max_length=200)
    created=models.DateTimeField(auto_now=True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True, blank=True)

    def save_profile(self):
        self.save()
    

    @classmethod
    def search_by_title(cls,searched_term):
        project = cls.objects.filter(title__icontains=searched_term)
        return project

    def __str__(self):
        return(self.title)

RATE_CHOICES=[
    (1,'1 - Could do better'),
    (2,'2 - Keep trying' ),
    (3,'3 - Almost there,'),
    (4,'4 - Nice'),
    (5, '5 - I like the effort put in this'),
    (6, '6 - Good'),
    (7, '7 - Very Goood'),
    (8, '8 -  woooooow!'),
    (9, '9 - Perfect'),
    (10, '10 - Amazing'),
]


class Review(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    # comment=models.CharField(max_length=200)
    rate_by_design=models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    rate_by_usability=models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    rate_by_content=models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    like=models.PositiveIntegerField(default=0)
    unlike=models.PositiveIntegerField(default=0)
    created=models.DateTimeField(auto_now=True)
    projects=models.ForeignKey(Projects,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return(self.user.username)

