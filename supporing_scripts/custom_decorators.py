import time

def get_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        wrapper.total_time += duration
        print(f"{'Execution time' :<15} : {duration:.3f} seconds")
        return result
    wrapper.total_time = 0
    return wrapper