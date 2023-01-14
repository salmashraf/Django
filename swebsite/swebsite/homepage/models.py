from django.db import models

# Create your models here.

class Books(models.Model):
    year=[("1800","1800-1900"),("1900","1900-2000"),("2000","2000-Now")]
    category = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    Publish_year = models.CharField(default="default", choices = year , max_length=30)
    Author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    image = models.ImageField (upload_to= 'photos/%y/%m/%d')
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.category
    class Meta:
        ordering = ['name']
        verbose_name = "My Library"
