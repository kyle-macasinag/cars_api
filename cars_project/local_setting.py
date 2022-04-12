# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*27+z(zk*5#spt$kb)4)+bfcfd*k5g7%u3-9-t#3nxc+4@w6vq'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "cars_database",
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}