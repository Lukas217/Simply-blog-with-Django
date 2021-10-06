from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'status',
        'crated_by',
        'created_date',
        'update_date',
        'publish_date',
    )
    list_filter = (
        'title',
        'slug',
        'status',
        'crated_by',
        'created_date',
        'update_date',
        'publish_date',
    )
    search_fields = (
        'title',
        'body'
    )
    prepopulated_fields = {'slug': ('title',)}
