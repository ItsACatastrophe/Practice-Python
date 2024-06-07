from typing import List
from random import randint


def main(l1: List[int], l2: List[int]):
    return [e for e in set(l1) if e in l2]  # I love 1 liners


def generate_int_list(length: int, max_value: int):
    return [
        randint(0, max_value if not length else length) for i in range(0, length + 1)
    ]


if __name__ == "__main__":
    l1 = [i for i in range(0, 11)]
    l2 = generate_int_list(5, 10)

    l1.sort()
    l2.sort()

    result = main(l1, l2)
    result.sort()

    print(f"li: {l1}")
    print(f"l2: {l2}")
    print(f"unique intersection: {result}")
