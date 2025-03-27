from django.apps import AppConfig
import threading
from .tasks import store_db_users_on_cache, generate_users_pdf_report

class ApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Application'

    def ready(self):
        """
            Execute tasks once this Django App is ready.
        """
        #threading.Thread(target=store_db_users_on_cache).start()
        #threading.Thread(target=generate_users_pdf_report).start()