from typing import Tuple, Dict


class Handler:

    def __init__(self, methods: Tuple):
        self._methods = methods or ('GET', )

    def get(self, func, request, *args, **kwargs):
        func_result = func(request)
        return f"GET: {func_result}"

    def post(self, func, request, *args, **kwargs):
        func_result = func(request)
        return f"POST: {func_result}"

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            method_request = request.get('method', 'GET')

            if method_request not in self._methods:
                return None
            if method_request == 'GET':
                return self.get(func, request)
            elif method_request == 'POST':
                return self.post(func, request)

        return wrapper
