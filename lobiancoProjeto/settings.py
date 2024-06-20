import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações de segurança
SECRET_KEY = 'django-insecure-*kh*19_nrtc2f9p1%(2gisd=2_&&z@o7^4*b+76^4!oc^c6a15'
DEBUG = True  # Defina como False em produção
ALLOWED_HOSTS = [".vercel.app"]

# Configuração dos aplicativos
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'home',
    'shows',
]

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''  # Seu usuário de email
EMAIL_HOST_PASSWORD = ''  # Sua senha de email
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

ACCOUNT_EMAIL_VERIFICATION = 'none'

# Configuração do middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'lobiancoProjeto.urls'

# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lobiancoProjeto.wsgi.application'

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.fdvermdxctbffplxamyu',
        'PASSWORD': 'LucasPassos*220705',
        'HOST': 'aws-0-sa-east-1.pooler.supabase.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalização
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]


# Arquivos de mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuração do campo de chave primária padrão
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações de autenticação
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_ADAPTER = 'home.adapters.CustomAccountAdapter'
