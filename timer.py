def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print(f"[*] Время выполнения функции {func.__name__}: {end - start} секунд.")
        return return_value

    return wrapper
