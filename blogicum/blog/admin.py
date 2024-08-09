from django.contrib import admin

from .models import Location, Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category'
    )

    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)


admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
