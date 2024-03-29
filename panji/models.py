from django.db import models

# Create your models here.


# Home
class Home(models.Model):
    name = models.CharField(max_length=20)
    greatings_1 = models.CharField(max_length=5)
    greatings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    # to save time for modification 
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
# About
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    profile_img = models.ImageField(upload_to='profile/')
    
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)
    
# Skills
class Skills(models.Model):
    skill_image = models.ImageField(upload_to='skill/', null=True, blank=True)

    def __str__(self):
        return f'Skills {self.id}'
    
    
# Portfolio Section

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return f'Portfolio {self.id}'
    