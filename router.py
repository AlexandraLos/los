#!usr/bin/python3.7.3
# -*- coding: utf-8 -*-


class Router:

    def __init__(self):
        self.methods = {}

    def add_path(self, path, method, func):
        self.path = path
        self.method = method
        if method not in self.methods:
            self.methods[self.method] = (self.path, func)

    def request(self, method, path):
        for key, value in self.methods.items():
            if key.upper() == method.upper():
                our_path, func = value
                if our_path == path:
                    return func()
                else:
                    return 404, "Error 404: Not Found"
        else:
            return 405, "Error 405: Method Not Allowed"

    def get(self, path):
        return self.request("GET", path)

    def post(self, path):
        return self.request("POST", path)

    def put(self, path):
        return self.request("PUT", path)

    def patch(self, path):
        return self.request("PATCH", path)

    def delete(self, path):
        return self.request("DELETE", path)

    def options(self, path):
        return self.request("OPTIONS", path)


def my_info():
    return 200, {"me": "Joanne"}

def update_me():
    return 200, "OK"


if __name__ == "__main__":
    router = Router()
    router.add_path('/me', 'GET', my_info)
    router.add_path('/me', 'UPDATE', update_me)
    print(router.request('get', '/me'))  # => 200, {"me": "Joanne"}
    print(router.get('/me'))  # => 200, {"me": "Joanne"}
    print(router.post('/me'))  # => 405, 'Error 405: Method Not Allowed'
    print(router.get('/us'))  # => 404, 'Error 404: Not Found'