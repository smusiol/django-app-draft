# Debug options
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG = True
TEMPLATE_DEBUG = True

# Database options

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite',
    }
}