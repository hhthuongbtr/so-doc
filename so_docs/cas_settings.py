## CAS config

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'django_cas_ng.backends.CASBackend',
    'so_docs.backends.MyCASBackend',
)

CAS_SERVER_URL = 'https://django-cas-ng-demo-server.herokuapp.com/cas/'
CAS_SERVER_URL = 'https://login.vng.com.vn/sso/'
CAS_VERSION = '3'
#CAS_CREATE_USER = False

# Config for Nginx proxy
CAS_ROOT_PROXIED_AS = "https://docs.mto.zing.vn"
#CAS_REDIRECT_URL = "https://google.com/"
CAS_STORE_NEXT= True
## END Cas

