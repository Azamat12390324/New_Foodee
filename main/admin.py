from django.contrib import admin
from main.models import Home, About, Feature, Menu_Category, Menu


@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    #list_filter = ('created_at',)


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('about_title', 'article')
    list_display_links = ('about_title',  'article')
    #list_filter = ('created_at',)



@admin.register(Feature)
class Feature(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    #list_filter = ('created_at',)



@admin.register(Menu_Category)
class Menu_Category(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    #list_filter = ('created_at',)



@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('title', 'category', 'food_name', 'food_price')
    list_display_links = ('title','category', 'food_name', 'food_price')
    #list_filter = ('created_at',)
