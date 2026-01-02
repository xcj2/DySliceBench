import sys,bisect,heapq
def I(): return(int(sys.stdin.readline()))
def LI(): return([int(x) for x in sys.stdin.readline().split()])
def S(): return(input())

def GCD(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def LCM(a,b):
    return a*b*GCD(a,b)

def main():
    s = S()
    l = 0
    r = len(s)-1
    ans = 0

    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        elif s[l] == "x":
            ans += 1
            l += 1
        elif s[r] == "x":
            ans += 1
            r -= 1
        else:
            ans = -1
            break
    return(ans)


if __name__ == "__main__":
    print(main())
