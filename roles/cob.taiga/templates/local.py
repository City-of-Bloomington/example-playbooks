from common import *

MEDIA_URL = "http://{{ taiga_hostname }}/media/"
STATIC_URL = "http://{{ taiga_hostname }}/static/"
ADMIN_MEDIA_PREFIX = "http://{{ taiga_hostname }}/static/admin/"
SITES["front"]["scheme"] = "http"
SITES["front"]["domain"] = "{{ taiga_hostname }}"

SECRET_KEY = "{{ taiga_secret_key }}"

DEBUG = False
TEMPLATE_DEBUG = False
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "{{ taiga_from_email }}"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Uncomment and populate with proper connection parameters
# for enable email sending. EMAIL_HOST_USER should end by @domain.tld
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_USE_TLS = False
#EMAIL_HOST = "localhost"
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
#EMAIL_PORT = 25

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"

