import sys
import itertools
input = sys.stdin.readline


def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def main():
    n = I()
    mylist = ("M", "A", "R", "C", "H")
    mylist2 = [0 for i in range(5)]
    for i in range(n):
        word = input().rstrip()[0]
        for i, k in enumerate(mylist):
            if word == k:
                mylist2[i] += 1
    mylist2 = [i for i in mylist2 if i != 0]
    
    
    if len(mylist2) <= 2:
        print(0)
        sys.exit()
    result = 0
    for a, b, c in itertools.combinations(mylist2, 3):
        result += a * b * c
    print(result)
    
main()