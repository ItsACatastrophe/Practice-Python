from random import randint


def main(values: list[str]):
    # A more typical case of this syntax would be: [f(v) for v in values]
    print([v for v in values if v < 10])


if __name__ == "__main__":
    list_length = randint(5, 10)
    main([randint(0, 20) for i in range(list_length)])
