from django.contrib import admin

from applications.feedback.models import Rating, Comment, Favorite, Like

admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Like)