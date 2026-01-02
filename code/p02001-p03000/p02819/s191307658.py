import sys
import math
input = sys.stdin.readline

def multiples(n):
    for i in range(3,100003):
        yield i*n
        if i*n > 100003:
            break

def sosuu(x):
    if x == 2 : return 2
    d = set()
    end = math.ceil(math.sqrt(x))
    d = d.union(multiples(2))
    for i in range(3,end,2):
        if i not in d:
            d = d.union(set(multiples(i)))
    
    i = x if x % 2 != 0 else x+1
    while True:
        if i not in d:
            return i
        i += 2

def main():
    x = int(input())
    print(sosuu(x))

if __name__ == "__main__":
    main()