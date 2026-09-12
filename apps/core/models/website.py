import uuid

from django.conf import settings
from django.db import models
from django.utils.safestring import mark_safe
from django_ckeditor_5.fields import CKEditor5Field


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        related_name="%(app_label)s_%(class)s_created",
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        related_name="%(app_label)s_%(class)s_updated",
    )

    class Meta:
        abstract = True

class Setting(BaseModel):

    STATUS = (
        ("True", "True"),
        ("False", "False"),
    )

    site_name = models.CharField(max_length=150)

    logo = models.ImageField(
        upload_to="settings/",
        blank=True,
        null=True,
    )

    favicon = models.ImageField(
        upload_to="settings/",
        blank=True,
        null=True,
    )

    offer_img = models.ImageField(
        upload_to="settings/",
        blank=True,
        null=True,
    )

    search_bg = models.ImageField(
        upload_to="settings/",
        blank=True,
        null=True,
    )

    testmonial_bg = models.ImageField(
        upload_to="settings/",
        blank=True,
        null=True,
    )

    # Colors
    header_footer_color = models.CharField(
        max_length=150,
        blank=True,
    )

    text_color = models.CharField(
        max_length=150,
        blank=True,
    )

    button_color = models.CharField(
        max_length=150,
        blank=True,
    )

    rera_color = models.CharField(
        max_length=150,
        blank=True,
    )

    # RERA
    rera_number = models.CharField(
        max_length=150,
        blank=True,
    )

    current_project_rera = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    # Google
    googletagmanager = models.CharField(
        max_length=150,
        blank=True,
    )

    google_map = models.CharField(
        max_length=1000,
        blank=True,
    )

    # Contact
    address = models.CharField(
        max_length=500,
        blank=True,
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
    )

    whatsapp = models.CharField(
        max_length=15,
        blank=True,
    )

    email = models.EmailField(
        max_length=100,
        blank=True,
    )

    # SMTP
    smtpserver = models.CharField(
        max_length=100,
        blank=True,
    )

    smtpemail = models.EmailField(
        max_length=100,
        blank=True,
    )

    smtppassword = models.CharField(
        max_length=100,
        blank=True,
    )

    smtpport = models.CharField(
        max_length=10,
        blank=True,
    )

    # Working hours
    working_days = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Mon - Sun",
    )

    working_hours = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: 10:00 AM - 6:00 PM",
    )

    # SEO
    meta_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    meta_description = models.TextField(
        blank=True,
        null=True,
    )

    meta_keywords = models.TextField(
        blank=True,
        null=True,
    )

    # Footer
    footer_text = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )

    copy_right = models.CharField(
        max_length=100,
        blank=True,
    )

    # Legal pages
    privacy_policy = CKEditor5Field(
        blank=True,
    )

    terms_conditions = CKEditor5Field(
        blank=True,
    )

    disclaimer = CKEditor5Field(
        blank=True,
    )

    cookies = CKEditor5Field(
        blank=True,
    )

    # Social Media
    facebook = models.CharField(
        max_length=255,
        blank=True,
    )

    instagram = models.CharField(
        max_length=255,
        blank=True,
    )

    twitter = models.CharField(
        max_length=255,
        blank=True,
    )

    youtube = models.CharField(
        max_length=255,
        blank=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default="True",
    )

    class Meta:
        verbose_name = "Website Setting"
        verbose_name_plural = "0. Website Settings"

    def __str__(self):
        return self.site_name

    def logo_tag(self):
        if self.logo:
            return mark_safe(
                f'<img src="{self.logo.url}" width="100" '
                f'style="object-fit:contain;border-radius:6px;">'
            )

        return "No Logo"

    logo_tag.short_description = "Logo"

class Slider(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="sliders",
    )

    title1 = models.CharField(
        max_length=200,
    )

    title2 = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    title3 = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    subtitle = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    badge_title = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    descriptions = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to="hero/",
    )

    button_text = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    button_link = models.URLField(
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Slider"
        verbose_name_plural = "1. Sliders"

    def __str__(self):
        return self.title1

class About(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="about_sections",
    )

    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    subtitle = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    content = CKEditor5Field(
        blank=True,
        null=True,
    )

    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True,
    )

    mission_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    mission_content = CKEditor5Field(
        blank=True,
        null=True,
    )

    vision_title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )

    vision_content = CKEditor5Field(
        blank=True,
        null=True,
    )

    years_of_experience = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    happy_families = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    square_feet = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    rera = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "2. About Section"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or "About"

class Milestone(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="milestones",
    )

    year = models.CharField(
        max_length=50,
    )

    title = models.CharField(
        max_length=200,
    )

    content = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Milestone"
        verbose_name_plural = "3. Milestones"
        ordering = ["year"]

    def __str__(self):
        return f"{self.year} - {self.title}"


class Contact_Page(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="contact_pages",
    )

    heading = models.CharField(
        max_length=200,
    )

    sub_heading = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    address = models.TextField()

    phone = models.CharField(
        max_length=20,
    )

    email = models.EmailField()

    map_iframe = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "3. Contact Pages"

    def __str__(self):
        return self.heading

class Our_Team(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="team_members",
    )

    name = models.CharField(
        max_length=100,
    )

    designation = models.CharField(
        max_length=100,
    )

    image = models.ImageField(
        upload_to="team/",
        blank=True,
        null=True,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "4. Our Team"

    def __str__(self):
        return self.name

class Testimonial(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="testimonials",
    )

    name = models.CharField(
        max_length=100,
    )

    designation = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    message = models.TextField()

    image = models.ImageField(
        upload_to="testimonial/",
        blank=True,
        null=True,
    )

    rating = models.PositiveIntegerField(
        default=5,
    )

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "5. Testimonials"

    def __str__(self):
        return f"{self.name} ({self.rating}⭐)"

class Why_Choose(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="why_choose_items",
    )

    icons = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Example: fa-solid fa-star",
    )

    title = models.CharField(
        max_length=200,
    )

    subtitle = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Why Choose"
        verbose_name_plural = "6. Why Choose Us"

    def __str__(self):
        return self.title



class FAQ(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="faqs",
    )

    question = models.CharField(
        max_length=300,
    )

    answer = CKEditor5Field()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "7. FAQs"

    def __str__(self):
        return self.question

class ImpactMetric(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="impact_metrics",
    )

    title = models.CharField(
        max_length=255,
    )

    value = models.CharField(
        max_length=100,
        help_text='Example: "10,000+" or "95%"',
    )

    icon = models.CharField(
        max_length=500,
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Impact Metric"
        verbose_name_plural = "8. Impact Metrics"

    def __str__(self):
        return f"{self.title}: {self.value}"



class Gallery(BaseModel):

    GALLERY_CHOICES = [
        ("project", "Projects"),
        ("events", "Events"),
        ("awards", "Awards"),
        ("amenities", "Amenities"),
        ("construction", "Construction"),
        ("interior", "Interior"),
        ("exterior", "Exterior"),
    ]

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="gallery_items",
    )

    gallery_category = models.CharField(
        max_length=25,
        choices=GALLERY_CHOICES,
        default="project",
        blank=True,
    )

    title = models.CharField(
        max_length=255,
    )

    image = models.ImageField(
        upload_to="gallery/",
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    featured = models.BooleanField(
        default=False,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Gallery"
        verbose_name_plural = "9. Gallery"

    def __str__(self):
        return self.title

class Enquiry(BaseModel):

    setting = models.ForeignKey(
        Setting,
        on_delete=models.CASCADE,
        related_name="enquiries",
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )

    message = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "10. Enquiries"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name or 'Unknown'} - {self.phone or 'No Phone'}"

class PropertyEnquiry(BaseModel):

    STATUS_CHOICES = (
        ('new', 'New Lead'),
        ('contacted', 'Contacted'),
        ('visit_scheduled', 'Site Visit Scheduled'),
        ('closed', 'Closed / Booked'),
        ('lost', 'Lost / Not Interested'),
    )

    name = models.CharField(max_length=150, verbose_name="Full Name")
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    email = models.EmailField(max_length=255, verbose_name="Email Address")
    message = models.TextField(verbose_name="Message / Requirement")
    schedule_visit = models.DateField(blank=True, null=True, verbose_name="Schedule Visit Date")

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='new', verbose_name="Status",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Received At")

    class Meta:
        verbose_name = "Property Enquiry"
        verbose_name_plural = "Property Enquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone}"

class Services(BaseModel):

    Title = models.CharField(max_length=200, verbose_name="Service Title")
    Short_Description = models.CharField(max_length=300, verbose_name="Service Title")
    Description = CKEditor5Field(blank=True, null=True, verbose_name="Service Description")
    icon = models.CharField(max_length=50, verbose_name="Service Title")


    def __str__(self):
        return self.Title

class Services_KeyPoints(BaseModel):

    Title = models.CharField(max_length=200, verbose_name="Service Title")
    Short_Description = models.CharField(max_length=300, verbose_name="Service Title")
    icon = models.CharField(max_length=50, verbose_name="Service Title")


    def __str__(self):
        return self.Title