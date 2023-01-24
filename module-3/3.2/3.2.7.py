from typing import Dict


class HandlerGET:

    def __init__(self, func):
        self.__func = func

    def get(self, func, request, *args, **kwargs):
        if request.get('method', 'GET') != 'GET':
            return None
        else:
            request_method = 'GET'

        func_result = func(request)
        return f'{request_method}: {func_result}'

    def __call__(self, request: Dict):
        return self.get(self.__func, request)


@HandlerGET
def contact(request: Dict) -> str:
    return "Сергей Балакирев"
