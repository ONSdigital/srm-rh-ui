import os

class Config(object):
    PORT = os.getenv("PORT", 8082)
    DEBUG = True


class DevelopmentConfig(Config):
    pass

class TestingConfig(DevelopmentConfig):
    pass