import math
import sys

sup = 1000000

is_prime = [0] * sup

count = [0] * sup

def setup():
    is_prime[2] = 1
    for n in range(3,sup,2):
        flag = True
        for i in range(3, int(math.floor(math.sqrt(n) + 1)), 2):
            if n % i == 0:
                flag = False
                break
        if flag:
            is_prime[n] = 1

def precount():
    for n in range(2, sup):
        count[n] = count[n-1] + is_prime[n]

def main():
    setup()
    precount()

    l = []

    for line in sys.stdin:
        l.append(int(line))

    for line in l:
         print(count[line])

if __name__ == "__main__":
    main()
