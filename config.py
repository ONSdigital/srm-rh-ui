import os


class BaseConfig:
    PORT = os.getenv("PORT")
    HOST = os.getenv('HOST')
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
    RH_SVC_URL = os.getenv("RH_SVC_URL")
    DOMAIN_URL = os.getenv("DOMAIN_URL")
    DOMAIN_URL_PROTOCOL = os.getenv("DOMAIN_URL_PROTOCOL")

    # Account service url is a link back to our service that we send to eq as part of the token
    ACCOUNT_SERVICE_URL = f"{DOMAIN_URL_PROTOCOL}{DOMAIN_URL}"
    LANGUAGES = ['en', 'cy']
    EQ_URL = os.getenv('EQ_URL')
    GTM_CONTAINER_ID = os.getenv('GTM_CONTAINER_ID')
    GTM_TAG_ID = os.getenv('GTM_TAG_ID')


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    PORT = os.getenv("PORT", 9093)
    HOST = os.getenv('HOST', '0.0.0.0')
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")
    EQ_URL = os.getenv('EQ_URL', 'http://localhost:5000')
    SECRET_KEY = os.getenv('SECRET_KEY', b'_5#y2L"F4Q8z\n\xec]/')
    DOMAIN_URL = os.getenv("DOMAIN_URL", "localhost:9092")
    DOMAIN_URL_PROTOCOL = os.getenv("DOMAIN_URL_PROTOCOL", 'http://')

    ACCOUNT_SERVICE_URL = f"{DOMAIN_URL_PROTOCOL}{DOMAIN_URL}"
    RH_SVC_URL = os.getenv("RH_SVC_URL", "http://localhost:8071/")
    GTM_CONTAINER_ID = os.getenv('GTM_CONTAINER_ID', 'GTM_CONTAINER_ID_XXXXX')
    GTM_TAG_ID = os.getenv('GTM_TAG_ID', 'GTM_TAG_ID_XXXXX')


class TestingConfig(DevelopmentConfig):
    DEBUG = False
