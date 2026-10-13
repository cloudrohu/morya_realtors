import math
from django.contrib import admin
from apps.blog.models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Admin list view me show hone waale fields
    list_display = ('name', 'slug', 'article_count')
    # Automatic slug generation
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

    # Dynamic method category me kitne articles hain count dikhane ke liye
    def article_count(self, obj):
        return obj.articles.count()
    article_count.short_description = "Total Articles"


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'author',
        'is_published',
        'created_at',
        'read_time',
    )

    list_filter = (
        'is_published',
        'category',
        'author',
        'created_at',
    )

    search_fields = (
        'title',
        'excerpt',
        'content',
    )

    ordering = ('-created_at',)



    list_editable = (
        'is_published',
    )


    prepopulated_fields = {
        'slug': ('title',)
    }


    readonly_fields = (
        'created_at',
        'updated_at',
        'read_time',
    )



    fieldsets = (

        (
            'Article Overview',
            {
                'fields': (
                    'title',
                    'slug',
                    'category',
                    'author',
                    'is_published',
                )
            }
        ),

        (
            'Content & Media',
            {
                'fields': (
                    'featured_image',
                    'excerpt',
                    'content',
                )
            }
        ),

        (
            'Article Information',
            {
                'classes': ('collapse',),
                'fields': (
                    'read_time',
                    'created_at',
                    'updated_at',
                )
            }
        ),
    )


    def save_model(self, request, obj, form, change):

        if not obj.author_id:
            obj.author = request.user

        super().save_model(
            request,
            obj,
            form,
            change
        )
