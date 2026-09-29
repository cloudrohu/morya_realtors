import math
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


def generate_unique_slug(instance, source_field, slug_field="slug"):
    """
    Generates a unique slug for a model instance.
    Appends a numeric suffix (-1, -2, etc.) if a duplicate exists.
    """
    base_slug = slugify(getattr(instance, source_field))
    if not base_slug:
        base_slug = "untitled"
        
    slug = base_slug
    model_class = instance.__class__
    
    # Exclude the current instance if it's an update
    qs = model_class.objects.filter(**{slug_field: slug})
    if instance.pk:
        qs = qs.exclude(pk=instance.pk)
        
    counter = 1
    while qs.exists():
        slug = f"{base_slug}-{counter}"
        qs = model_class.objects.filter(**{slug_field: slug})
        if instance.pk:
            qs = qs.exclude(pk=instance.pk)
        counter += 1
        
    return slug


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, 'name')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='blog_posts'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='articles'
    )
    featured_image = models.ImageField(upload_to='blog/images/', null=True, blank=True)
    excerpt = models.TextField(max_length=300, help_text="A short summary displayed on the blog card.")
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, 'title')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    @property
    def read_time(self):
        words = len(self.content.split())
        minutes = math.ceil(words / 200) if words > 0 else 1
        return f"{minutes} min read"

    @property
    def author_initials(self):
        first = self.author.first_name[0] if self.author.first_name else ""
        last = self.author.last_name[0] if self.author.last_name else ""
        initials = f"{first}{last}".upper()
        return initials if initials else self.author.username[:2].upper()