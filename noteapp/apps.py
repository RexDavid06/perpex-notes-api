from django.apps import AppConfig


class NoteappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'noteapp'

    def ready(self):
        import noteapp.signals # this ensures that the signals are imported when the app is ready
