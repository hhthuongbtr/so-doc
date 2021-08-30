
LOGGING = {
    "version": 1,
	"disable_existing_loggers": True,
    "formatters":{ 
        "console": {
            "format":"%(asctime)s - serverity: %(levelname)s - %(pathname)s:%(lineno)d - message: %(message)s"
        },
        "mkdocs":{
            "format":"mkdocs: date: %(asctime)s - %(name)s - p%(process)s %(pathname)s:%(lineno)d - serverity: %(levelname)s - message: %(message)s"
        },
        "django":{
            "format":"Django: date: %(asctime)s - %(name)s - p%(process)s %(pathname)s:%(lineno)d - serverity: %(levelname)s - message: %(message)s"
        }
    },
    "handlers": {
        "mkdocs": {
            "filename": "logs/mkdocs.log",
            "encoding": "utf8",
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "mkdocs"
        },
        "django":{
            "filename": "logs/django.log",
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "django"
        },
        "console":{
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "console"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": ["mkdocs"]
    },
    "loggers": {
        "console": {
            "handlers": ["console"],
            "level": "DEBUG"
        },
        "all": {
            "handlers": ["mkdocs", "django"],
            "level": "DEBUG"
        }
    }
}

