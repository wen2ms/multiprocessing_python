import multiprocessing
from time import sleep


def foo(args):
    sleep(2)

    print(args)


class Worker(multiprocessing.Process):
    def run(self):
        foo("bar")


if __name__ == "__main__":
    # must add ","
    worker = multiprocessing.Process(target=foo, args=("foo",))
    worker.start()
    worker.join()

    worker = Worker()
    worker.start()
    worker.join()
