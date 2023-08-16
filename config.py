import os


class BaseConfig():
    PORT = os.getenv("PORT", 9092)
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
    RH_SVC_URL = os.getenv("RH_SVC_URL", "http://localhost:8071/")
    ACCOUNT_SERVICE_URL = os.getenv("ACCOUNT_SERVICE_URL", "http://localhost:9092/")
    LANGUAGES = ['en', 'cy']
    EQ_URL = os.getenv('EQ_URL')


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")
    EQ_URL = os.getenv('EQ_URL', 'http://localhost:5000')


class TestingConfig(DevelopmentConfig):
    pass
