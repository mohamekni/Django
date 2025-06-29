from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'


class SuiteConfig(DjangoSuitConfig):
    layout = 'vertical'