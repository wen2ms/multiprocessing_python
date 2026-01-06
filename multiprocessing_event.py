import time
from multiprocessing import Event, Process


def bus(event):
    print("Bus is comming")
    time.sleep(3)
    print("Bus arrived")
    event.set()


def passenger(name, event):
    print(name, "is waiting")
    event.wait()
    print(name, "Go")


if __name__ == "__main__":
    event = Event()
    processes = []
    process = Process(target=bus, args=(event,))
    process.start()
    processes.append(process)

    for i in range(10):
        process = Process(
            target=passenger,
            args=(f"passenger{i}", event),
        )
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
