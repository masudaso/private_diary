from .settings_common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-z9xyp_*l$xb82_*j1vhbp(y(6i#g7$xt6v&n640+#g%vy%vqd%"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
    "version": 1,  # 1固定
    "disable_existing_loggers": False,
    # ロガーの設定
    "loggers": {
        # Djangoが利用するロガー
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        # diaryアプリケーションが利用するロガー
        "diary": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
    # ハンドラの設定
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev",
        },
    },
    # フォーマッタの設定
    "formatters": {
        "dev": {
            "format": "\t".join(
                [
                    "%(asctime)s",
                    "[%(levelname)s]",
                    "%(pathname)s(Line:%(lineno)d)",
                    "%(message)s",
                ]
            )
        },
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
