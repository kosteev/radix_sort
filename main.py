import itertools
import random
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        res = func(*args, **kwargs)
        print('Time for {}: {}'.format(func.__name__, time.time() - t))
        return res

    return wrapper


@timeit
def python_sort(a):
    return sorted(a)


@timeit
def radix_sort(a):
    m = 16
    size = 1 << m

    max_a = max(a)
    decades = 0
    while max_a:
        decades += 1
        max_a >>= m

    shift = 0
    while decades:
        by_key = [
            []
            for _ in range(size)
        ]

        for t in a:
            by_key[(t >> shift) & (size - 1)].append(t)

        a = list(itertools.chain(*by_key))
        shift += m
        decades -= 1

    return a


if __name__ == '__main__':
    a = [
        random.randint(0, 1000 * 1000 * 1000)
        for _ in range(100 * 1000 * 1000)
    ]

    assert python_sort(a) == radix_sort(a)
