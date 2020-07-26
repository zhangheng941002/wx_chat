"""
Django settings for yk_wx project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-xo-6j1+9n%1@7s-9jus=d50kw@+vqn62*i_30nvqbnhm=5iq='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',

    "send_msg",
    "other",
    "ftp_web",
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

ROOT_URLCONF = 'yk_wx.urls'

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

WSGI_APPLICATION = 'yk_wx.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

LOVE_MSG = ['我什么时候能变成风，然后就可以一直吻你。',
            '遇见喜欢，大概就像一艘从来不靠岸的船终于找到港湾。',
            '没有一种不通过蔑视，忍受和奋斗就可以征服的命运。',
            '只是想和你在一起简单平淡足以。',
            '俄只是觉得喜欢和爱不同，仅此而已。',
            '找你害怕烦到你，不找你，我真的很想你。',
            '每一杯普通的水，和喜欢的人在一起就会变成雪碧。',
            '你是我的东，你是我的西，你是我的南，你是我的北。',
            '小的时候不懂爱‘但心中却充满爱，N年后明白了什么叫爱‘所以再也没爱过。',
            '生活中值得高兴的事情太多，别把目光都盯在那些让你不愉快的事情上。',
            '爱的时候想着一个人是快乐的。',
            '据说手机24小时从不关机的，人心中都有一个让他牵挂的人。',
            '爱你的人不会轻易离开，轻易离开你的人也许没那么爱你。',
            '幸福是，两双眼睛，看一个未来。',
            '爱会磨平你一身的棱角，褪去你一身的骄傲。',
            '不能阻止他人的非议，自己活得自在才好！只要你相信你自己是善良的，那就OK了。',
            '借我一刻光阴，把你看的真切，绾正青丝白雪。',
            '喜欢你的声音，喜欢你爱我，他其实，是她一直的梦想。',
            '爱一个人，爱到八分刚刚好，所有的期待和希望希望都只有七，八分，剩下的两三分用来爱自己。',
            '被你喜欢过，真的很难觉得别人有那么喜欢我。',
            '面对着白纸，却不知道该怎么抒写我们的感情。',
            '如果下一秒就要分离，上一秒我也要努力吻你。',
            '用手挡住射进眼里的阳光，就像挡住对你的思念，挡不住。',
            '我只希望我们都好好的。好好的笑，好好的过，好好的一辈子。',
            '我愿用我一世容颜换你半世流离。',
            '很多时候，都是最后才领悟，而爱情，却不能重头再来。',
            '我的生活朴实无华，但正是因为有了你而变得豪华。',
            '你如果觉得我的爱是枷锁，我宁可背上所有，也要牢牢的铐住你让你离不开我。',
            '我愿化作你的天使，永远守候在你的身边。',
            '希望有一天，我可以不用对着手机屏幕和你说晚安，你就在我身边。',
            '不管我们之前遇到过什么人，现在只想你是我的最后一个故事。',
            '爱你就像呼吸，有时调皮地憋一会儿，可终究知道对于停止爱你，我无能为力。',
            '我爱你，如鲸向海、鸟投林，不可避免，退无可退。',
            '把前半生都给你，后半生我就潦草收场吧。',
            '当你驯服我，我将赠予你，虔诚的爱恋，以及不悔的决心。',
            '一辈子住在一个地方，一辈子睡在一个人身边。',
            '被爱着的她，连撑伞的样子都像捧着一束玫瑰花。',
            '爱让我义无反顾扮演了硬派，也让我们歇斯底里变成病态。',
            '你说是我们相见恨晚，我说为爱你不够勇敢。',
            '我的幸福，就是和你温暖的过一辈子。',
            '爱你就算会经历暴风雨，还是不离不弃陪着你。',
            '你笑起来的样子最好看，你的声音最好听，更令人开心的是你是我的。',
            '不管怎样我都觉得你是最好的，这就是偏爱，偏爱是不需要理由的。',
            '把你的名字刻在烟上，吸进肺里，留在离我心里最近的地方。',
            '多陪陪女朋友，她没有篮球，没有游戏，只有你。',
            '你最好的给予，就是还能让我留在你的身边。',
            '不再甜言蜜语，不是感情淡了，而是成熟了，知道要用行动兑现自己的承诺。',
            '把自己当衣服给你穿，换你暖，遮你羞，避你寒，悉心装扮，衬你好看。',
            '有哪本教科书，可以教我如何留住你的心？',
            '整个世界，我最爱的地方就是你的左右。',
            '十指连心，我握住了你的手指，是不是也能握住你的心？',
            '我的心很完整是因为，你在里面。',
            '爱的如此虚伪，伤的如此彻底。',
            '爱就要在一起，不爱就会放弃。',
            '喜欢你的人除了我还有很多，但我只有你。',
            '待我白发苍苍，你会不会依旧如此，给我倾世温柔？',
            '我穿越四季只为融化在你怀里，谢谢你敢与我相爱。',
            '累了吗，停在我怀里吧，我给你一生的安定。',
            '我们谁都没有联系谁，可是我却一直在想你。',
            '如果可以，我想陪你一起疯，就像陪你蹲下做一只蘑菇一样。',
            '和你说话时，你可要好好看看，我脑海中的弹幕，因为，里面全是爱你的小句子。']


# 好友发送天气信息默认值
LOVE = "备用"
LOVE_WHERE = "昌平"
PROVINCE = "北京"
WEATHER_DAYS = 3

WEEK_MAP = {
    "1": "星期一",
    "2": "星期二",
    "3": "星期三",
    "4": "星期四",
    "5": "星期五",
    "6": "星期六",
    "7": "星期日",
}

# 高德API信息，可自己注册申请
GD_URL = "https://restapi.amap.com/v3"
GD_KEY = "90e03aba500340813a84061f3e28c525"

# 腾讯智能机器人，请自己申请
TX_KEY = "2125667918"
TX_TOKEN = "YBCQnC3q4PLQAGNN"

FTP_CONFIG = {
    "IP": "0.0.0.0",  # 服务器IP
    "USERNAME": "zh",
    "PASSWORD": "123456",
    "FILE_PATH": "/env",  # 映射的路径
    "PORT": 21,
    "MAX_CONS": 1024,
    "MAX_CONS_PER_IP": 1024,
}

try:
    from .pro_conf import *
except Exception as e:
    print(e)
