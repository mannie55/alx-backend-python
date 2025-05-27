def expand(cases):
    def decorator(func):
        def wrapper(self):
            for case in cases:
                with self.subTest(case=case):
                    func(self, *case)
        return wrapper
    return decorator