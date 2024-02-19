import osimport os

# Other settings...

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


os.environ.setdefault(
    "DATABASE_URL", "postgres://uqjblnv8ooz:X3ppY4Ah97dm@ep-gentle-mountain-a23bxz6h.eu-central-1.aws.neon.tech/class_quota_genre_673893")
