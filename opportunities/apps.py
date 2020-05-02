from django.apps import AppConfig


class OpportunitiesConfig(AppConfig):
    name = 'opportunities'

    def ready(self):
        from . import updater
        updater.start()
        print("I will scrape habibe")
