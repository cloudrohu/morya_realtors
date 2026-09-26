"""
Base Django settings for Findexors CRM
"""

from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, True),
)

environ.Env.read_env(BASE_DIR / ".env")


SECRET_KEY = env(
    "SECRET_KEY",
    default="django-insecure-change-me",
)

DEBUG = env.bool("DEBUG", default=True)
ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=[
        "127.0.0.1",
        "192.168.1.3",
        "localhost",
    ],
)

AUTH_USER_MODEL = "accounts.User"


DJANGO_APPS = [
   # "grappelli",
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "crispy_forms",
    "crispy_bootstrap5",
    "import_export",
    "django_ckeditor_5",
    "multiselectfield",
    "embed_video",
]
LOCAL_APPS = [
    "apps.accounts.apps.AccountsConfig",
    "apps.core.apps.CoreConfig",
    "apps.utility.apps.UtilityConfig",

    "apps.blog.apps.BlogConfig",
    "apps.outscraper.apps.OutscraperConfig",
    "apps.job.apps.JobConfig",
    "apps.job_utility.apps.JobUtilityConfig",

    "apps.crm.apps.CrmConfig",
    "apps.companies.apps.CompaniesConfig",
    "apps.customers.apps.CustomersConfig",
    "apps.enquiries.apps.EnquiriesConfig",
    "apps.followups.apps.FollowupsConfig",
    "apps.meetings.apps.MeetingsConfig",
    "apps.tasks.apps.TasksConfig",
    "apps.reports.apps.ReportsConfig",
    "apps.response.apps.ResponseConfig",
    "apps.dashboard.apps.DashboardConfig",
   # "apps.business.apps.BusinessConfig",
   # "apps.business_utility.apps.BusinessUtilityConfig",
   "apps.properties.apps.PropertiesConfig",
   "apps.properties_utility.apps.PropertiesUtilityConfig",
   "apps.importer",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ------------------------------------------------------------------------------
# MIDDLEWARE
# ------------------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

# ------------------------------------------------------------------------------
# TEMPLATES
# ------------------------------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ------------------------------------------------------------------------------
# DATABASE
# ------------------------------------------------------------------------------

DATABASES = {
    "default": env.db(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# ------------------------------------------------------------------------------
# PASSWORDS
# ------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ------------------------------------------------------------------------------
# INTERNATIONALIZATION
# ------------------------------------------------------------------------------

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"

USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------------------------
# STATIC
# ------------------------------------------------------------------------------

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ------------------------------------------------------------------------------
# MEDIA
# ------------------------------------------------------------------------------

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------------------------------------------------------------
# STORAGES
# ------------------------------------------------------------------------------

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# ------------------------------------------------------------------------------
# CRISPY
# ------------------------------------------------------------------------------

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ------------------------------------------------------------------------------
# REST FRAMEWORK
# ------------------------------------------------------------------------------

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
}

# ------------------------------------------------------------------------------
# LOGIN
# ------------------------------------------------------------------------------

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"




CKEDITOR_5_CONFIGS = {

    "default": {

        "toolbar": [
            "heading",
            "|",

            "fontFamily",
            "fontSize",
            "fontColor",
            "fontBackgroundColor",

            "|",

            "bold",
            "italic",
            "underline",
            "strikethrough",
            "subscript",
            "superscript",

            "|",

            "link",
            "insertImage",
            "mediaEmbed",

            "|",

            "bulletedList",
            "numberedList",
            "todoList",

            "|",

            "alignment",
            "outdent",
            "indent",

            "|",

            "blockQuote",
            "code",
            "codeBlock",

            "|",

            "insertTable",
            "horizontalLine",

            "|",

            "specialCharacters",

            "|",

            "undo",
            "redo",
        ],

        "fontFamily": {
            "options": [
                "default",
                "Arial, Helvetica, sans-serif",
                "Georgia, serif",
                "Times New Roman, Times, serif",
                "Verdana, Geneva, sans-serif",
                "Tahoma, Geneva, sans-serif",
                "Trebuchet MS, sans-serif",
                "Courier New, Courier, monospace",
            ],
            "supportAllValues": True,
        },

        "fontSize": {
            "options": [
                "tiny",
                "small",
                "default",
                "big",
                "huge",
            ],
            "supportAllValues": True,
        },

        "fontColor": {
            "colors": [
                {
                    "color": "#000000",
                    "label": "Black",
                },
                {
                    "color": "#FFFFFF",
                    "label": "White",
                },
                {
                    "color": "#C89B2C",
                    "label": "Gold",
                },
                {
                    "color": "#B89252",
                    "label": "Brown Gold",
                },
                {
                    "color": "#D6B77A",
                    "label": "Light Gold",
                },
                {
                    "color": "#FF0000",
                    "label": "Red",
                },
                {
                    "color": "#00A651",
                    "label": "Green",
                },
                {
                    "color": "#0066FF",
                    "label": "Blue",
                },
                {
                    "color": "#800080",
                    "label": "Purple",
                },
                {
                    "color": "#808080",
                    "label": "Gray",
                },
            ],
        },

        "fontBackgroundColor": {
            "colors": [
                {
                    "color": "#FFFFFF",
                    "label": "White",
                },
                {
                    "color": "#000000",
                    "label": "Black",
                },
                {
                    "color": "#FFF3CD",
                    "label": "Light Yellow",
                },
                {
                    "color": "#D1E7DD",
                    "label": "Light Green",
                },
                {
                    "color": "#CFE2FF",
                    "label": "Light Blue",
                },
                {
                    "color": "#F8D7DA",
                    "label": "Light Red",
                },
                {
                    "color": "#E2E3E5",
                    "label": "Light Gray",
                },
            ],
        },

        "alignment": {
            "options": [
                "left",
                "center",
                "right",
                "justify",
            ],
        },

        "image": {
            "toolbar": [
                "imageTextAlternative",
                "imageStyle:inline",
                "imageStyle:block",
                "imageStyle:side",
                "linkImage",
            ],
        },

        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
        },

        "link": {
            "addTargetToExternalLinks": True,
            "defaultProtocol": "https://",
            "decorators": {
                "openInNewTab": {
                    "mode": "manual",
                    "label": "Open in a new tab",
                    "attributes": {
                        "target": "_blank",
                        "rel": "noopener noreferrer",
                    },
                },
            },
        },

        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
                {
                    "model": "heading4",
                    "view": "h4",
                    "title": "Heading 4",
                    "class": "ck-heading_heading4",
                },
                {
                    "model": "heading5",
                    "view": "h5",
                    "title": "Heading 5",
                    "class": "ck-heading_heading5",
                },
                {
                    "model": "heading6",
                    "view": "h6",
                    "title": "Heading 6",
                    "class": "ck-heading_heading6",
                },
            ],
        },

        "htmlSupport": {
            "allow": [
                {
                    "name": "div",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "span",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "p",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "h1",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "h2",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "h3",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "h4",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "h5",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "h6",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "a",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "img",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "table",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "td",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
                {
                    "name": "th",
                    "classes": True,
                    "styles": True,
                    "attributes": True,
                },
            ],
        },

        "removePlugins": [],

    },

}