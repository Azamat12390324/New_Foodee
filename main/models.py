from django.db import models


class Home(models.Model):
    banner = models.ImageField(upload_to='banner/%Y/%m/%d')
    title = models.CharField(max_length=25)
     
    def __str__(self) -> str:
       return self.title
     
     
class About(models.Model):
    image_left = models.ImageField(upload_to='about/image_left/%Y/%m/%d')
    about_title =  models.CharField(max_length=255)
    descriptions = models.TextField()
    article = models.CharField(max_length=255, blank=True)
    article_author = models.CharField(max_length=255, blank=True)
    
    def __str__(self) -> str:
       return self.about_title
   
    class Meta:
       verbose_name = 'About'
       verbose_name_plural = 'Abouts'
       
     
    
class Feature(models.Model):
    icons =  models.ImageField(upload_to='Feature/icons/%Y/%m/%d', blank=True)
    title =  models.CharField(max_length=25, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    
    def __str__(self) -> str:
       return self.title
   
    class Meta:
       verbose_name = 'Feature'
       verbose_name_plural = 'Features'
       
     
    

class Menu_Category(models.Model):
    icons = models.ImageField(upload_to='Menu/icons/%Y/%m/%d', blank=True)
    title =  models.CharField(max_length=25, blank=True)

    def __str__(self) -> str:
       return self.title
   
    class Meta:
       verbose_name = 'Category'
       verbose_name_plural = 'Categories'
       
     

    
class Menu(models.Model):
    icons = models.ImageField(upload_to='Menu/icons/%Y/%m/%d', blank=True)
    title =  models.CharField(max_length=25, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Menu_Category, on_delete= models.CASCADE, blank=True)
    food_name = models.CharField(max_length=255, blank=True)
    food_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    food_image = models.ImageField(upload_to='media/Menu/food_image/%Y/%m/%d', blank=True)
    
    def __str__(self) -> str:
       return self.title
     

    class Meta:
       verbose_name = 'Menu'
       verbose_name_plural = 'Menus'
       
