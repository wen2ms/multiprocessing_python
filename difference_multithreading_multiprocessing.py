import multiprocessing
import threading
import time
from queue import Queue


def calc(queue):
    total = 0
    for i in range(10000000):
        total += i + i**2 + i**3
    queue.put(total)


def multicore():
    queue = multiprocessing.Queue()
    worker1 = multiprocessing.Process(target=calc, args=(queue,))
    worker2 = multiprocessing.Process(target=calc, args=(queue,))
    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()
    total = queue.get() + queue.get()
    print(f"muticore: {total}")


def multithreading():
    queue = Queue()
    worker1 = threading.Thread(target=calc, args=(queue,))
    worker2 = threading.Thread(target=calc, args=(queue,))
    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()
    total = queue.get() + queue.get()
    print(f"multihreading: {total}")


def normal():
    total = 0
    for _ in range(2):
        for i in range(10000000):
            total += i + i**2 + i**3
    print(f"normal: {total}")


if __name__ == "__main__":
    start = time.time()
    normal()
    end = time.time()
    print(f"normal time = {end - start}")

    start = time.time()
    multithreading()
    end = time.time()
    print(f"multithreading time = {end - start}")

    start = time.time()
    multicore()
    end = time.time()
    print(f"multicore time = {end - start}")
