from django.apps import AppConfig


class StattrackrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StatTrackr'
    verbose_name = 'Sports Statistics Tracker'

    def ready(self):
        """
        Initialize app configuration when Django starts.
        Import signals here to avoid any circular imports.
        """
        try:
            import StatTrackr.signals  # Create this file for any signals
        except ImportError:
            pass

        # You can add any startup initialization code here
        print(f"Initializing {self.verbose_name}...")