from django.apps import AppConfig

print("in appy.py")
class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
