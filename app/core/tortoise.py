from app.settings.config import settings
from .init_app import get_app_list

def get_tortoise_config() -> dict:
    app_list = get_app_list()
    app_list.append('aerich.models')
    config = {
        'connections': settings.DB_CONNECTIONS,
        'apps': {
            'models': {
                'models': app_list,
                'default_connection': 'default',
            }
        }
    }
    return config


TORTOISE_ORM = get_tortoise_config()