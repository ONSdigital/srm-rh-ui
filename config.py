import os


class BaseConfig():
    PORT = os.getenv("PORT", 9092)
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")
    #LANGUAGES = ["en", "cy"]
    LANGUAGES = ["cy", "en"]


class TestingConfig(DevelopmentConfig):
    pass
