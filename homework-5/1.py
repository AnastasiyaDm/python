# LRU (least recently used) — это алгоритм, при котором вытесняются значения, которые дольше всего не запрашивались.
# Соответственно, необходимо хранить время последнего запроса к значению. И как только число закэшированных значений
# превосходит N необходимо вытеснить из кеша значение, которое дольше всего не запрашивалось.
#
#
# Задача - 1
# Создать декоратор lru_cache(подобный тому который реализован в Python).
#
# Задача-2
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_info  - статистика использования вашего кеша(например: сколько раз вычислялась ваша функция,
# а сколько раз значение было взято из кеша, сколько места свободно в кеше)
#
# Задача-3
# Ваш lru_cache декоратор должен иметь служебный метод
# cache_clear - очищает кеш

from collections import OrderedDict
import functools


def lru_cache(maxsize=5):
    def decorator(func):
        cache = OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            if args and not kwargs:
                key = args
            elif args and kwargs:
                key = args + tuple(sorted(kwargs.items()))
            else:
                key = tuple(sorted(kwargs.items()))

            try:
                result = cache.pop(key)
                wrapper.hits += 1
            except KeyError:
                result = func(*args, **kwargs)
                wrapper.misses += 1

                if len(cache) >= maxsize:
                    cache.popitem()

            cache[key] = result

            return result

        def cache_info():
            print({
                'cache': dict(cache),
                'hits': wrapper.hits,
                'misses': wrapper.misses

            })

        def cache_clear():
            cache.clear()
            wrapper.hits = wrapper.misses = 0

        wrapper.hits = 0
        wrapper.misses = 0
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper

    return decorator


@lru_cache()
def main(a, b):
    return a + b


if __name__ == '__main__':
    main(10, b=20)
    main(5, b=2)
    main(10, b=2)
    main(10, b=20)
    main(5, b=2)
    main(8, b=7)
    main(6, b=4)
    main(8, b=7)
    main(8, b=8)


main.cache_info()
