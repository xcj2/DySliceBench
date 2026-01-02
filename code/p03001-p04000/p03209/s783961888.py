import math

def burger_size(n):
    return 2**(n + 2) - 3

def num_of_patty(n):
    return 2**(n + 1) - 1

def calc(n, x):
    if n == 0:
        return 1
    if x <= n:
        return 0
    if x == burger_size(n):
        return num_of_patty(n)
    
    center = math.floor((burger_size(n) + 1) / 2)
    if x < center:
        return calc(n - 1, x - 1)
    elif x > center:
        return num_of_patty(n - 1) + 1 + calc(n - 1, x - burger_size(n - 1) - 2)
    else:
        return num_of_patty(n - 1) + 1

n, x = [int(i) for i in input().split()]
print(calc(n, x))