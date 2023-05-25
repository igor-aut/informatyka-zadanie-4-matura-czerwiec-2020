import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

with open('pary.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    number, word = line.strip().split()
    number = int(number)

    if number % 2 == 0:
        found = False
        for i in range(3, number // 2 + 1, 2):
            if is_prime(i) and is_prime(number - i):
                print(number, i, number - i)
                found = True
                break
        if not found:
            print("Brak rozwiązania dla liczby", number)