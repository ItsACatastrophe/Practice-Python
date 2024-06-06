def main():

    numerator = int(input("Please supply a numerator of a fraction: "))
    denominator = int(input("Please supply a denominator of a fraction: "))

    print(
        f"Your fraction will {'*not* ' if numerator % denominator != 0 else '' }divide evenly!"
    )


if __name__ == "__main__":
    main()
