"""
Django settings for ShopProject project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '27vk=m&71(4i418o=rwlp*bl!7@zaulvbnb3^xm&+8snhza#pn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []
#允许所有主机访问
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #注册子应用
    #DRF基于token令牌认证的应用
    'rest_framework.authtoken',
    #自动生成API文档
    'coreapi',
    'rest_framework',
    'django_filters',
    'DjangoUeditor',
    'xadmin',
    'crispy_forms',
    'reversion',
    'app.goods', 'app.trade', 'app.user_operation','app.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ShopProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'ShopProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ShopProject',
        'USER': 'shopuser',
        'PASSWORD': 'westos',
        'HOST': '47.104.161.55',
        'PORT': '3306',
        #这里引擎用innodb（django默认为mysiam）
        "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"}
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'
#TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
AUTH_USER_MODEL = 'users.UserProfile'

# 设置上传文件的路径: http://xxxx/media/hello,png
MEDIA_URL = "/media/"
# 设置media的保存路径: media/hello.png
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
#分页设置
REST_FRAMEWORK = { #分页
                         'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
                    #每页显示的个数
                        'PAGE_SIZE': 10,
                    # 指定用于支持coreapi的Schema
                        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
                    'DEFAULT_AUTHENTICATION_CLASSES': (
                    # 此身份验证方案使用HTTP基本身份验证，根据用户的用户名和密码进行签名。仅用于测试。
                            'rest_framework.authentication.BasicAuthentication',
                    # 此身份验证方案使用Django的默认会话后端进行身份验证。
                            'rest_framework.authentication.SessionAuthentication',
                    # 此身份验证方案使用基于令牌的简单HTTP身份验证方案。令牌认证适用于客户端 - 服务器设 置。
                            #'rest_framework.authentication.TokenAuthentication' )
                    #使用jwt token认证
                            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',)
                }

import datetime
JWT_AUTH={
            #Token失效时间, 也可以设置seconds=20
           'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
            #Token前缀
            'JWT_AUTH_HEADER_PREFIX': 'JWT'
        }

AUTHENTICATION_BACKENDS = (
                    #'django.contrib.auth.backends.ModelBackend',
                    'app.users.views.CustomBackend', )

# 正则验证手机号码，11位数字，1开头，第二位数必须是3456789这些数字之一
# ^:以什么开头, $以什么结尾。 [3456789]字符集， 代表电话号码的第2位是3或者4或者....
REGEX_MOBILE = '^1[345789]\d{9}$'

# 云片网APIKEY
APIKEY = "xxxx"