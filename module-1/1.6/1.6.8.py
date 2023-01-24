TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:

    def __new__(cls, *args, **kwargs):
        name, *_ = args

        if TYPE_OS == 1:
            dialog_windows = DialogWindows()
            setattr(dialog_windows, 'name', name)

            return dialog_windows
        else:
            dialog_linux = DialogLinux()
            setattr(dialog_linux, 'name', name)

            return dialog_linux
