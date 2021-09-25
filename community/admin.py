from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'movie_title', 'title', 'rank', 'content')

admin.site.register(Review, ReviewAdmin)