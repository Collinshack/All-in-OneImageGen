from django.db import models
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    api_key = models.CharField(max_length=50, blank=True, null=True)
    
    
    
    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Users Detail'
        verbose_name_plural = 'Users Details'
   
    def __str__(self):
        return self.name
    

class Image(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    prompt = models.CharField(max_length=200)
    generated_image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.prompt
    
class QrCode(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    user_input = models.CharField(max_length=200)
    generated_qrcode = models.ImageField(upload_to='qrcodes')
    
    def __str__(self):
        return self.user_input
    
    
    
class Waitlist(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    more_features = models.CharField(max_length=2000, blank=True, null=True)
    
    def __str__(self):
        return self.email
    
class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date_published = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    
    