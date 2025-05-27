def expand(cases):
    def decorator(func):
        def wrapper(self):
            for case in cases:
                func(self, *case)
        return wrapper
    return decorator