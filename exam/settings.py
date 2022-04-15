import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q4u7+05es^0*9*z%f^0_9^1_ek#$sw2_qb5oj+y(&c3o99ie2&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'teacher',
    'account',
    'arrange',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', # 关闭csrf
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'exam.urls'

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

WSGI_APPLICATION = 'exam.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'exam',
        'USER': 'root',
        'PASSWORD': '3306066',
        'HOST': '101.43.66.34',
        'PORT': '3306',
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


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Chongqing'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
SIMPLEUI_DEFAULT_THEME = 'light.css'
SIMPLEUI_LOGO = '/static/admin/simpleui-x/img/logon.png'
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False
SIMPLEUI_CONFIG = {
    'system_keep': True,
    'menu_display': ['教师账号', '教师信息', '考试安排', '考试信息', '考试状态', '学院设置', '专业设置', "可视化" ],
    'menus': [
        {
            'name': '教师信息',
            'url': '/admin/teacher/teacher/'
        },
        {
            'name': '学院设置',
            'icon': 'fa fa-bed',
            'url': '/admin/teacher/college/'
        }
        ,{
            'name':'考试状态',
            'icon': 'fa fa-align-left',
            'url': '/admin/arrange/arrange/'
        },
        {
            'name': '系别设置',
            # 'icon': 'fa fa-address-card',
            'url': '/admin/teacher/department/'
        },
        {
            'name': '专业设置',
            'url': '/admin/teacher/profession/'
        },
        {
            'name': '教师账号',
            'icon': 'fa fa-address-card',
            'url': '/admin/account/account/'
        },
        {
            'name': '考试信息',
            'url': '/admin/arrange/exam/'
        }, 
        {
            'name': '考试安排',
            'icon': 'fa fa-align-center',
            'url': 'http://101.43.66.34:8082/exam/arrange'
        }, 
        {
            'name': '可视化',
            'icon': 'fa fa-adjust',
            'url': 'http://101.43.66.34:8083/index.html'
        }, 
    ]
}
