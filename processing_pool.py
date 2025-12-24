import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def square(num):
    return num**2


def two_square_sum(num1, num2):
    return num1**2 + num2**2


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    pool = multiprocessing.Pool(processes=2)
    print(pool.map(square, nums))
    result = pool.apply_async(square, (1,))
    print(result.get())
    results = [pool.apply_async(square, (num,)) for num in nums]
    print([result.get() for result in results])

    twos = [(1, 2), (3, 4)]
    print(pool.starmap(two_square_sum, twos))

    with ProcessPoolExecutor(max_workers=2) as executor:
        print(list(executor.map(square, nums)))

        futures = [executor.submit(square, num) for num in nums]
        print([future.result() for future in futures])

        print(list(executor.map(two_square_sum, *zip(*twos))))
