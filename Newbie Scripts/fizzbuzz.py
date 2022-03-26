import random


def randobuzz(max):
    count, fizzbuzz, fizz, buzz = 0, 0, 0, 0
    while count < max:
        count += 1
        random_number = random.randint(1, 100)
        if random_number % 5 == 0 and random_number % 3 == 0:
            print(f"{count}: {random_number}: FizzBuzz")
            fizzbuzz += 1
        elif random_number % 5 == 0:
            print(f"{count}: {random_number}: Fizz")
            fizz += 1
        elif random_number % 3 == 0:
            print(f"{count}: {random_number}: Buzz")
            buzz += 1
        else:
            print(f"{count}: {random_number}")
    others = count - (fizzbuzz + fizz + buzz)
    print(
        f"Total count: Fizzbuzz: {fizzbuzz}, Fizz: {fizz}, Buzz: {buzz}, Others: {others} ")


def orderedbuzz():
    for i in range(100):
        if i % 5 == 0 and i % 3 == 0:
            print(f"{i}: FizzBuzz")
        elif i % 5 == 0:
            print(f"{i}: Fizz")
        elif i % 3 == 0:
            print(f"{i}: Buzz")
        else:
            print(i)


random_number = 0
choice = str.lower(input("[R]andom FizzBuzz or [S]equntial FizzBuzz?"))
flag = True
max = 0

while flag is True:
    if choice == "r":
        max = int(input("Enter Limit: "))
        flag = False
        randobuzz(max)
    elif choice == "s":
        orderedbuzz()
        flag = False
