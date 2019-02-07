from os import environ


class Config:
    ...


class Development(Config):
    ...


class Production(Config):
    ...


class Testing(Config):
    ...


envs = {
    'config': Config,
    'development': Development,
    'production': Production,
    'testing': Testing,
}


def get_env():
    """Choose env class name."""
    return envs[environ.get('FLASK_ENV', default='config')]
