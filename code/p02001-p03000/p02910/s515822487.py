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
    s = S()
    for i in range(len(s)):
        if i%2==0 and s[i] == "L":
            return "No"
        if i%2==1 and s[i] == "R":
            return "No"
    return "Yes"

if __name__ == "__main__":
    print(main())
