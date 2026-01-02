import math
from functools import reduce

def gcdli(xl):
    #xlはlist
    return reduce(math.gcd , xl)

def gcd(a , b):
    while b != 0:
        a , b = b , a % b
    return a

def c162(k):

    count = 0
    li = []
    for i in range(1 , k + 1):
        for w in range(1 , k + 1):
            for q in range(1 , k + 1):
                li = [i , w , q]
                count += gcdli(li)
    """
    for i in range(1 , k + 1):
        for w in range(1 , k + 1):
            count += gcd(i , w)
    """
    return count

def main():
    k = int(input())
    print(c162(k))
if __name__ == '__main__':
    main()