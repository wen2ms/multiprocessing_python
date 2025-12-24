import multiprocessing
from time import sleep


def foo(value, num, lock):
    # lock.acquire()
    # lock.release()
    for _ in range(10):
        sleep(0.1)
        with lock:
            value.value += num
            print(value.value)


if __name__ == "__main__":
    lock = multiprocessing.Lock()
    value = multiprocessing.Value("i", 0)
    worker1 = multiprocessing.Process(target=foo, args=(value, 1, lock))
    worker2 = multiprocessing.Process(target=foo, args=(value, 3, lock))
    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()
