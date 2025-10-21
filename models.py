from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
 
class Member(models.Model):
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    hospital = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.hospital})"




class CarouselSlide(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to="carousel/")  # upload folder
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or " "
    
    
class NewsTicker(models.Model):
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
