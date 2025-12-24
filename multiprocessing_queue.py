import multiprocessing


def square_sum(results_queue, num):
    total = 0
    for i in range(num):
        total += i * i
    results_queue.put(total)


if __name__ == "__main__":
    results_queue = multiprocessing.Queue()
    worker1 = multiprocessing.Process(target=square_sum, args=(results_queue, 100))
    worker2 = multiprocessing.Process(target=square_sum, args=(results_queue, 100))
    worker1.start()
    worker2.start()
    worker1.join()
    worker2.join()
    total = results_queue.get() + results_queue.get()
    print(total)
