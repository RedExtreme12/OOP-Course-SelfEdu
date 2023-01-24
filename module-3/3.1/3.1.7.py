from copy import copy
from typing import List, Union


class AppVK:

    def __init__(self):
        self.name = 'ВКонтакте'


class AppYouTube:

    def __init__(self, memory_max):
        self.name = 'YouTube'
        self.memory_max = memory_max


class AppPhone:

    def __init__(self, phone_list: dict):
        self.name = 'Phone'
        self.phone_list = copy(phone_list)


class SmartPhone:

    def __init__(self, model: str):
        self.model = model
        self.apps: List[Union[AppVK, AppPhone, AppYouTube]] = []
        self._app_names = set()

    def get_apps_names(self):
        for app in self.apps:
            yield app

    def add_app(self, app: Union[AppVK, AppPhone, AppYouTube]):
        if app.name not in self._app_names:
            self.apps.append(app)
            self._app_names.add(app.name)

    def remove_app(self, app: Union[AppVK, AppPhone, AppYouTube]):
        self.apps.remove(app)
