# -*- coding: utf-8 -*-
"""
Django settings for lawyer_site project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5e7hdjgbo&1#2skrcuo#u!=+d8t0&w1pat(_40z6bhf4*19q0b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',
    'django_user_agents',
]

# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'lawyer_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'lawyer_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SUIT_CONFIG = {
    'MENU': (

        # Keep original label and models
        'sites',

        {'label': u'首页图片', 'icon': 'icon-cog', 'models': (
            {'model': 'index.IndexImages', 'label': u'轮播图'},
            {'model': 'index.IndexContent', 'label': u'轮播内容'},
        )},

        {'label': u'律师介绍', 'icon': 'icon-cog', 'models': (
            {'model': 'index.Lawyer', 'label': u'律师个人'},
            {'model': 'index.LawyerTeam', 'label': u'律师团队'},
            {'model': 'index.LawFirm', 'label': u'律所介绍'},
        )},

        {'label': u'律师服务', 'icon': 'icon-cog', 'models': (
            {'model': 'index.LawService', 'label': u'律师服务'},
        )},

        {'label': u'成功案例', 'icon': 'icon-cog', 'models': (
            {'model': 'index.LawyerCase', 'label': u'律师案例'},
            {'model': 'index.ClassicCase', 'label': u'经典案例'},
        )},

        {'label': u'法律法规', 'icon': 'icon-cog', 'models': (
            {'model': 'index.LegalProvisions', 'label': u'法律规定'},
            {'model': 'index.AdministrativeRegulations', 'label': u'行政法规'},
            {'model': 'index.JudicialInterpretation', 'label': u'司法解释'},
            {'model': 'index.OtherProvisions', 'label': u'其他规定'},
        )},

        {'label': u'法律新闻', 'icon': 'icon-cog', 'models': (
            {'model': 'index.IndustryNews', 'label': u'行业动态'},
            {'model': 'index.SociologyNews', 'label': u'法治社会'},
            {'model': 'index.LawNews', 'label': u'法律前沿'},
        )},

        {'label': u'律师交流', 'icon': 'icon-cog', 'models': (
            {'model': 'index.Business', 'label': u'业务交流'},
            {'model': 'index.Activity', 'label': u'活动交流'},
        )},

        {'label': u'咨询留言', 'icon': 'icon-cog', 'models': (
            {'model': 'index.Message', 'label': u'咨询留言'},
        )},
    )
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
