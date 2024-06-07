# Problem

> Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

I'm going to start treating "ask the user as input" as the arguments of the function. The whole input setup w/ mocking is not even close to the way most software works. Perhaps I'll use something like argparse eventually for a more serious way of parsing inputs but for now the function inputs and returns will count as "input" and "print"

# Solutions

## Unsorted Return Durations

- main(100000) = 0:00:00.046683
- main2(100000) = 0:00:00.024468
- main3(100000) = 0:00:00.000069 (unsorted) AND 0:00:00.000110 (sorted)

