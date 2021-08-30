import os
import yaml
from django.conf import settings
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(settings.BASE_DIR, 'staticfiles')

MKDOCS_CONFIG_FILE = 'mkdocs.yml'
MKDOCS_CONFIG = os.path.join(settings.BASE_DIR, MKDOCS_CONFIG_FILE)
DOCS_DIR = ''
DOCS_STATIC_NAMESPACE = ''
DOCS_BASE_DIR = ''
with open(MKDOCS_CONFIG, 'r') as f:
    DOCS_DIR = yaml.load(f, Loader=yaml.Loader)['site_dir']
    DOCS_STATIC_NAMESPACE = os.path.basename(DOCS_DIR)

DOCS_BASE_DIR = os.path.dirname(os.path.dirname(MKDOCS_CONFIG_FILE))
