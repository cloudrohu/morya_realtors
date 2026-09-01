from django.contrib import admin
from django.utils.html import format_html

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
)


# ============================================================
# COMMON INLINE
# ============================================================

class BaseSettingInline(admin.StackedInline):
    """
    Common inline configuration for all website sections.
    """

    extra = 1
    min_num = 0
    show_change_link = False
    can_delete = True
    classes = ()


# ============================================================
# SLIDER INLINE
# ============================================================

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

    extra = 1

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


# ============================================================
# ABOUT INLINE
# ============================================================

class AboutInline(BaseSettingInline):
    model = About

    fields = (
        # Home Content
        "title",
        "subtitle",
        "content",
        "read_legacy",
        "image",
        "image_preview",

        # About Content
        "about_title",
        "about_subtitle",
        "about_content",

        # Mission / Vision
        "mission_title",
        "mission_content",
        "vision_title",
        "vision_content",

        # Hero
        "hero_title",
        "hero_highlight",
        "hero_subtitle",
        "hero_description",
        "hero_background",
        "hero_background_preview",

        "button_one_text",
        "button_one_link",

        "button_two_text",
        "button_two_link",

        # SEO
        "seo_title",
        "seo_description",

        # Images
        "right_image1",
        "right_image1_preview",
        "right_image2",
        "right_image2_preview",

        # Stats
        "years_of_experience",
        "happy_families",

        "is_active",
    )

    readonly_fields = (
        "image_preview",
        "hero_background_preview",
        "right_image1_preview",
        "right_image2_preview",
    )

    extra = 1

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.image.url,
            )
        return "No Image"

    image_preview.short_description = "Main Image Preview"

    def hero_background_preview(self, obj):
        if obj and obj.hero_background:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:cover; border:1px solid #ddd; padding:5px;" />',
                obj.hero_background.url,
            )
        return "No Image"

    hero_background_preview.short_description = "Hero Background Preview"

    def right_image1_preview(self, obj):
        if obj and obj.right_image1:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.right_image1.url,
            )
        return "No Image"

    right_image1_preview.short_description = "Right Image 1 Preview"

    def right_image2_preview(self, obj):
        if obj and obj.right_image2:
            return format_html(
                '<img src="{}" style="max-height:120px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.right_image2.url,
            )
        return "No Image"

    right_image2_preview.short_description = "Right Image 2 Preview"


# ============================================================
# CONTACT PAGE INLINE
# ============================================================

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

    extra = 1


# ============================================================
# OUR TEAM INLINE
# ============================================================

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

    extra = 1

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="height:100px; width:100px; '
                'object-fit:cover; border-radius:8px; border:1px solid #ddd;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


# ============================================================
# TESTIMONIAL INLINE
# ============================================================

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

    extra = 1

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="height:100px; width:100px; '
                'object-fit:cover; border-radius:50%; border:1px solid #ddd;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


# ============================================================
# WHY CHOOSE INLINE
# ============================================================

class WhyChooseInline(BaseSettingInline):
    model = Why_Choose

    fields = (
        "icons",
        "title",
        "subtitle",
        "order",
        "is_active",
    )

    extra = 1


# ============================================================
# FAQ INLINE
# ============================================================

class FAQInline(BaseSettingInline):
    model = FAQ

    fields = (
        "question",
        "answer",
        "is_active",
    )

    extra = 1


# ============================================================
# IMPACT METRIC INLINE
# ============================================================

class ImpactMetricInline(BaseSettingInline):
    model = ImpactMetric

    fields = (
        "title",
        "value",
        "icon",
        "order",
        "is_active",
    )

    extra = 1


# ============================================================
# GALLERY INLINE
# ============================================================

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

    extra = 1

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" style="max-height:150px; max-width:250px; '
                'object-fit:contain; border:1px solid #ddd; padding:5px;" />',
                obj.image.url,
            )

        return "No Image"

    image_preview.short_description = "Preview"


# ============================================================
# ENQUIRY INLINE
# ============================================================

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

    extra = 1


# ============================================================
# SETTING ADMIN
# ============================================================

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

        # ====================================================
        # WEBSITE INFORMATION
        # ====================================================

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

        # ====================================================
        # THEME COLORS
        # ====================================================

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

        # ====================================================
        # RERA
        # ====================================================

        (
            "RERA Information",
            {
                "fields": (
                    "rera_number",
                    "current_project_rera",
                )
            },
        ),

        # ====================================================
        # CONTACT
        # ====================================================

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

        # ====================================================
        # WORKING HOURS
        # ====================================================

        (
            "Working Hours",
            {
                "fields": (
                    "working_days",
                    "working_hours",
                )
            },
        ),

        # ====================================================
        # GOOGLE / SMTP
        # ====================================================

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

        # ====================================================
        # SOCIAL MEDIA
        # ====================================================

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

        # ====================================================
        # SEO
        # ====================================================

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

        # ====================================================
        # FOOTER
        # ====================================================

        (
            "Footer",
            {
                "fields": (
                    "footer_text",
                    "copy_right",
                )
            },
        ),

        # ====================================================
        # LEGAL
        # ====================================================

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

        # ====================================================
        # STATUS
        # ====================================================

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

    # ========================================================
    # ALL WEBSITE SECTIONS INLINE
    # ========================================================

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
    ]

    # ========================================================
    # LOGO PREVIEW
    # ========================================================

    def logo_preview(self, obj):
        if obj and obj.logo:
            return format_html(
                '<img src="{}" style="height:60px; max-width:180px; '
                'object-fit:contain; border:1px solid #ddd; padding:4px;" />',
                obj.logo.url,
            )

        return "No Logo"

    logo_preview.short_description = "Logo"