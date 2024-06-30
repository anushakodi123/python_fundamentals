import time
import threading
import concurrent.futures


def timer_decorator(func):
    def wrapper(num):
        start_time = time.time()
        result = func(num)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time}")
        return result

    return wrapper


@timer_decorator
def calculate_squares_normal(numbers):
    res = []
    for i in range(1, numbers + 1):
        time.sleep(0.1)
        res.append(i * i)
    return res


@timer_decorator
def calculate_squares_threaded(numbers):
    def cal_squares(n, squares):
        time.sleep(0.1)
        squares.append(n * n)

    threads = []
    squares = []

    for n in range(1, numbers + 1):
        thread = threading.Thread(target=cal_squares, args=(n, squares))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return squares


numbers = 100

print("Normal calculation:", calculate_squares_normal(numbers))

print("Threaded calculation:", calculate_squares_threaded(numbers))




def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")