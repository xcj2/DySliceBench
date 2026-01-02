import sys
import heapq
import bisect

mod = 10**9+7
dd = ((-1,0),(1,0),(0,-1),(0,1))

def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return((list(sys.stdin.readline()))[:-1])

def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def LCM(a,b):
    return a * b // GCD(a,b)

def main():
    s = input()
    if s == "Sunny":
        return "Cloudy"
    if s == "Cloudy":
        return "Rainy"
    if s == "Rainy":
        return "Sunny"

if __name__ == "__main__":
    print(main())
