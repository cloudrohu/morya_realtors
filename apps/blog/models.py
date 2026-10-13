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

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles"
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_articles"
    )

    author_designation = models.CharField(
        max_length=100,
        default="Real Estate Experts",
        blank=True
    )

    featured_image = models.ImageField(
        upload_to="blog/images/",
        null=True,
        blank=True
    )

    excerpt = models.TextField(
        max_length=300,
        help_text="Short summary displayed below the article title."
    )

    content = models.TextField(
        help_text="Complete article content."
    )

    tags = models.CharField(
        max_length=500,
        blank=True,
        help_text="Comma separated tags. Example: Mumbai, Real Estate, Property"
    )

    is_published = models.BooleanField(
        default=True
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )


    meta_title = models.CharField(
        max_length=255,
        blank=True
    )

    meta_description = models.TextField(
        max_length=300,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Article.objects.filter(
                slug=slug
            ).exclude(
                pk=self.pk
            ).exists():

                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    # =========================
    # ARTICLE URL
    # =========================

    def get_absolute_url(self):
        return reverse(
            "blog:blog_detail",
            kwargs={"slug": self.slug}
        )

    # =========================
    # READ TIME
    # =========================

    @property
    def read_time(self):

        words = len(self.content.split())

        minutes = math.ceil(words / 200) if words else 1

        return f"{minutes} min read"

    # =========================
    # AUTHOR NAME
    # =========================

    @property
    def author_name(self):

        full_name = self.author.get_full_name()

        return full_name or self.author.username

    # =========================
    # AUTHOR INITIALS
    # =========================

    @property
    def author_initials(self):

        first = (
            self.author.first_name[0]
            if self.author.first_name
            else ""
        )

        last = (
            self.author.last_name[0]
            if self.author.last_name
            else ""
        )

        initials = f"{first}{last}".upper()

        return initials or self.author.username[:2].upper()

    # =========================
    # TAG LIST
    # =========================

    @property
    def tag_list(self):

        return [
            tag.strip()
            for tag in self.tags.split(",")
            if tag.strip()
        ]

    # =========================
    # PREVIOUS ARTICLE
    # =========================

    @property
    def previous_article(self):

        return (
            Article.objects
            .filter(
                is_published=True,
                created_at__gt=self.created_at
            )
            .order_by("created_at")
            .first()
        )


    @property
    def next_article(self):

        return (
            Article.objects
            .filter(
                is_published=True,
                created_at__lt=self.created_at
            )
            .order_by("-created_at")
            .first()
        )