import os


class BaseConfig():
    PORT = os.getenv("PORT", 9092)
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
    RH_SVC_URL = os.getenv("RH_SVC_URL", "http://localhost:8071/")
    ACCOUNT_SERVICE_URL = os.getenv("ACCOUNT_SERVICE_URL", "http://localhost:9092/")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "DEBUG")


class TestingConfig(DevelopmentConfig):
    pass
