from django.apps import AppConfig

class AuctionsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "auctions_app"
    verbose_name: str = "Auctions App"
