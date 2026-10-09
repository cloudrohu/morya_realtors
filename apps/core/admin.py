from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django_ckeditor_5.widgets import CKEditor5Widget
from django_ckeditor_5.fields import CKEditor5Field

from .models.website import (
    Setting,
    Slider,
    Why_Choose,
    About,
    Contact_Page,
    Enquiry,
    Our_Team,
    Testimonial,
    FAQ,
    ImpactMetric,
    Gallery,
    PropertyEnquiry,
    Milestone,
    Services,
    Services_KeyPoints,
)


class BaseSettingInline(admin.StackedInline):
    """
    Common inline configuration for all website sections.
    """

    extra = 1
    min_num = 0
    show_change_link = False
    can_delete = True
    classes = ()


class SliderInline(BaseSettingInline):
    model = Slider

    fields = (
        "title1",
        "title2",
        "title3",
        "subtitle",
        "badge_title",
        "descriptions",
        "image",
        "image_preview",
        "button_text",
        "button_link",
        "order",
        "is_active",
    )

    readonly_fields = (
        "image_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


class AboutInline(BaseSettingInline):
    model = About

    # 1. Force CKEditor5Widget on the field types used in this inline
    formfield_overrides = {
        CKEditor5Field: {'widget': CKEditor5Widget(config_name='default')},
        models.TextField: {'widget': CKEditor5Widget(config_name='default')},
    }

    fields = (
        "title",
        "subtitle",
        "content",
        "image",
        "image_preview",
        "mission_title",
        "mission_content",
        "vision_title",
        "vision_content",
        "years_of_experience",
        "happy_families",
        "square_feet",
        "rera",
        "is_active",
    )

    readonly_fields = (
        "image_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Main Image Preview"


class MilestoneInline(BaseSettingInline):
    model = Milestone

    fields = (
        "year",
        "title",
        "content",
        "is_active",
    )

    extra = 0

class ContactPageInline(BaseSettingInline):
    model = Contact_Page

    fields = (
        "heading",
        "sub_heading",
        "address",
        "phone",
        "email",
        "map_iframe",
        "is_active",
    )

    extra = 0


class OurTeamInline(BaseSettingInline):
    model = Our_Team

    fields = (
        "name",
        "designation",
        "image",
        "image_preview",
        "bio",
        "is_active",
    )

    readonly_fields = (
        "image_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="height:100px; width:100px; '
                'object-fit:cover; border-radius:8px; border:1px solid #ddd;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


class TestimonialInline(BaseSettingInline):
    model = Testimonial

    fields = (
        "name",
        "designation",
        "message",
        "image",
        "image_preview",
        "rating",
        "is_active",
    )

    readonly_fields = (
        "image_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="height:100px; width:100px; '
                'object-fit:cover; border-radius:50%; border:1px solid #ddd;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


class WhyChooseInline(BaseSettingInline):
    model = Why_Choose

    fields = (
        "icons",
        "title",
        "subtitle",
        "order",
        "is_active",
    )

    extra = 0


class FAQInline(BaseSettingInline):
    model = FAQ

    fields = (
        "question",
        "answer",
        "is_active",
    )

    extra = 0

class ImpactMetricInline(BaseSettingInline):
    model = ImpactMetric

    fields = (
        "title",
        "value",
        "icon",
        "order",
        "is_active",
    )

    extra = 0


class GalleryInline(BaseSettingInline):
    model = Gallery

    fields = (
        "gallery_category",
        "title",
        "image",
        "image_preview",
        "description",
        "featured",
        "order",
        "is_active",
    )

    readonly_fields = (
        "image_preview",
    )

    extra = 0

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="max-height:150px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


class EnquiryInline(BaseSettingInline):
    model = Enquiry

    fields = (
        "name",
        "email",
        "phone",
        "message",
        "is_active",
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )

    extra = 0


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):

    list_display = (
        "site_name",
        "status",
        "phone",
        "email",
        "logo_preview",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "status",
        "is_active",
    )

    search_fields = (
        "site_name",
        "phone",
        "email",
        "rera_number",
        "address",
    )

    readonly_fields = (
        "logo_preview",
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Website Information",
            {
                "fields": (
                    "site_name",
                    "logo",
                    "logo_preview",
                    "favicon",
                    "offer_img",
                    "search_bg",
                    "testmonial_bg",
                )
            },
        ),


        (
            "Theme Colors",
            {
                "fields": (
                    "header_footer_color",
                    "text_color",
                    "button_color",
                    "rera_color",
                )
            },
        ),
        
        (
            "Construction Status",
            {
                "fields": (
                    "new_launch",
                    "under_construction",
                    "ready_to_move_in",
                )
            },
        ),

        (
            "RERA Information",
            {
                "fields": (
                    "rera_number",
                    "current_project_rera",
                )
            },
        ),


        (
            "Contact Information",
            {
                "fields": (
                    "address",
                    "phone",
                    "whatsapp",
                    "email",
                    "google_map",
                )
            },
        ),

        (
            "Working Hours",
            {
                "fields": (
                    "working_days",
                    "working_hours",
                )
            },
        ),


        (
            "Google & SMTP",
            {
                "fields": (
                    "googletagmanager",
                    "smtpserver",
                    "smtpemail",
                    "smtppassword",
                    "smtpport",
                )
            },
        ),

        (
            "Social Media",
            {
                "fields": (
                    "facebook",
                    "instagram",
                    "twitter",
                    "youtube",
                )
            },
        ),

        (
            "SEO",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "meta_keywords",
                )
            },
        ),

        (
            "Footer",
            {
                "fields": (
                    "footer_text",
                    "copy_right",
                )
            },
        ),

        (
            "Legal Pages",
            {
                "fields": (
                    "privacy_policy",
                    "terms_conditions",
                    "disclaimer",
                    "cookies",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "status",
                    "is_active",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


    inlines = [
        SliderInline,
        AboutInline,
        ContactPageInline,
        OurTeamInline,
        TestimonialInline,
        WhyChooseInline,
        FAQInline,
        ImpactMetricInline,
        GalleryInline,
        EnquiryInline,
        MilestoneInline,
    ]

    class Media:
        css = {
            'all': ('django_ckeditor_5/dist/styles.css',)
        }
        js = ('django_ckeditor_5/dist/bundle.js',)


    def logo_preview(self, obj):
        if obj and obj.logo:
            return format_html(
                '<img src="{}" style="height:60px; max-width:180px; '
                'object-fit:contain; border:1px solid #ddd; padding:4px;" />',
                obj.logo.url,
            )

        return "No Logo"

    logo_preview.short_description = "Logo"

@admin.register(PropertyEnquiry)
class PropertyEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'schedule_visit', 'status', 'created_at')
    list_filter = ('status', 'schedule_visit', 'created_at')
    search_fields = ('name', 'phone', 'email', 'message')
    list_editable = ('status',)
    date_hierarchy = 'created_at'
    list_per_page = 25


class ServicesKeyPointsInline(admin.TabularInline):
    """Allows editing key points directly within the main Service admin page."""

    model = Services_KeyPoints
    extra = 0
    fields = ("Title", "Short_Description", "icon")


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("Title", "Short_Description", "icon")
    search_fields = ("Title", "Short_Description")
    inlines = [ServicesKeyPointsInline]


@admin.register(Services_KeyPoints)
class ServicesKeyPointsAdmin(admin.ModelAdmin):
    list_display = ("Title", "Short_Description", "icon")
    search_fields = ("Title", "Short_Description")

