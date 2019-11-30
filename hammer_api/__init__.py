from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'hammer_api'

    def ready(self):
        pass
