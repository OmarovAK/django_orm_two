from django.apps import AppConfig


class ModelMigrateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_migrate'
