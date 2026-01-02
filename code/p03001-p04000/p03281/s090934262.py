import math

def input_number():
    return int(input())

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

def is_8(number):
    fraction_of_the_number = 0
    for i in range(1, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            fraction_of_the_number += 2
    if fraction_of_the_number == 8 and is_odd(number):
        return True
    else:
        return False

def main():
    n = input_number()
    answer = 0
    for i in range(1, n+1, 2):
        if is_8(i):
            answer += 1
    print(answer)

main()