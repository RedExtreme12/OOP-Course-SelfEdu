class Application:

    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:

    instance = None
    applications = dict()

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)

        return cls.instance

    def add_application(self, app: Application):
        self.applications[app.name] = app

    def remove_application(self, app: Application):
        self.applications.pop(app.name)

    def block_application(self, app: Application):
        self.applications[app.name].blocked = True

    def total_apps(self) -> int:
        return len(self.applications)


# store = AppStore()
# app_youtube = Application("Youtube")
#
# store.add_application(app_youtube)
#
# print(store.applications)
#
# store.block_application(app_youtube)
#
# print(store.applications[app_youtube.name].blocked)
#
# store.remove_application(app_youtube)
#
# print(store.applications)
