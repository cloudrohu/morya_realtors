from django.shortcuts import render, get_object_or_404
from apps.core.models.website import Setting
from apps.blog.models import Article, Category


def get_settings():
    """Helper function to fetch settings object safely"""
    return Setting.objects.first()


def blog_list(request):
    articles = Article.objects.filter(is_published=True).select_related('author', 'category')
    categories = Category.objects.all()

    context = {
        'settings_obj': get_settings(),
        'articles': articles,
        'categories': categories,
    }

    return render(request, 'home/blog_list.html', context)


def blog_detail(request, slug):
    article = get_object_or_404(
        Article.objects.select_related('author', 'category'),
        slug=slug,
        is_published=True
    )

    recent_articles = Article.objects.filter(is_published=True).exclude(id=article.id)[:4]

    context = {
        'settings_obj': get_settings(),
        'article': article,
        'recent_articles': recent_articles,
    }

    return render(request, 'home/blog_details.html', context)