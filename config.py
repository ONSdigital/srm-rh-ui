import os


class BaseConfig:
    PORT = os.getenv("PORT")
    HOST = os.getenv('HOST')
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
    RH_SVC_URL = os.getenv("RH_SVC_URL")
    ACCOUNT_SERVICE_URL = os.getenv("ACCOUNT_SERVICE_URL")
    LANGUAGES = ['en', 'cy']
    EQ_URL = os.getenv('EQ_URL')
    GTM_CONTAINER_ID = os.getenv('GTM_CONTAINER_ID')
    GTM_TAG_ID = os.getenv('GTM_TAG_ID')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    PORT = os.getenv("PORT", 9092)
    HOST = os.getenv('HOST', '0.0.0.0')
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")
    EQ_URL = os.getenv('EQ_URL', 'http://localhost:5000')
    SECRET_KEY = os.getenv('SECRET_KEY', b'_5#y2L"F4Q8z\n\xec]/')
    RH_SVC_URL = os.getenv("RH_SVC_URL", "http://localhost:8071/")
    ACCOUNT_SERVICE_URL = os.getenv("ACCOUNT_SERVICE_URL", "http://localhost:9092/")
    GTM_CONTAINER_ID = os.getenv('GTM_CONTAINER_ID', 'GTM_CONTAINER_ID_XXXXX')
    GTM_TAG_ID = os.getenv('GTM_TAG_ID', 'GTM_TAG_ID_XXXXX')


class TestingConfig(DevelopmentConfig):
    pass
