from django.apps import AppConfig


class CustomiseappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customiseapp'
