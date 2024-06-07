from datetime import datetime
from math import ceil, floor, sqrt


# Fine
def main(value: int):
    divisors = []

    for i in range(1, value + 1):
        if value % i == 0:
            divisors.append(i)

    return divisors


# Fast
def main2(value: int):
    divisors = []

    for i in range(1, floor(value / 2) + 1):
        if value % i == 0:
            divisors.append(i)

    divisors.append(value)

    return divisors


# Blazingly Fast!
def main3(value: int):
    divisors = []

    for i in range(1, ceil(sqrt(value))):
        if value % i == 0:
            divisors.append(i)

            num = value / i
            if i != num:
                divisors.append(int(num))

        # if i != (value / i):
        #     tmp = i * i
        #     if tmp != value:
        #         divisors.append(tmp)

    divisors.sort(key=lambda e: e)

    return divisors


if __name__ == "__main__":
    start = datetime.now()
    main(1000000)
    print(datetime.now() - start)

    start = datetime.now()
    main2(1000000)
    print(datetime.now() - start)

    start = datetime.now()
    main3(1000000)
    print(datetime.now() - start)
