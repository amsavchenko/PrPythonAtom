def cache_decorator(function):
    cache = {}

    def cached_function(argument):
        if argument in cache.keys():
            return cache[argument]
        else:
            cache[argument] = function(argument)
            return cache.get(argument)
    return cached_function



@cache_decorator
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-2) + fib(n-1)
