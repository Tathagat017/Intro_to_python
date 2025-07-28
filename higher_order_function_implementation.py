def custom_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

def custom_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

def custom_reduce(func, iterable, initializer=None):
    iterator = iter(iterable)
    if initializer is None:
        accumulator = next(iterator)
    else:
        accumulator = initializer
    for item in iterator:
        accumulator = func(accumulator, item)   
    return accumulator