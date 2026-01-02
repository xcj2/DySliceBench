import sys
import math

def input():
    return sys.stdin.readline().strip()

def iinput():
    return int(input())

def finput():
    return float(input())

def tinput():
    return input().split()

def rinput():
    return map(int, tinput())

def rlinput():
    return list(rinput())

def pro(k, l, n):
    if l < n:
        if k == 0:
            return(n - l)
        return (n - l + 2)
    if l == n:
        if k == 0:
            return 0
        elif k == 1:
            return 1
        return 3
    else:
        l -= n - 1
        if l == k:
            return 1
        elif l > k:
            return 0
        if l < k - 1:
            return 2
        else:
            return 3
            

def rt(k, l , n):
    if k < n:
        if l == 0:
            return (k * 2 + n)
        return (n + k * 2 - 1)
    elif k == n:
        if l == 1:
            return (k * 3 - 2)
        elif l == 0:
            return (k * 3)
        return (k * 3 - 3)
    else:
        k -= n - 1
        if k == l:
            return (n * 3 - 2)
        elif k > l:
            return (n * 3)
        if k < l - 1:
            return ((n - 1) * 3 - 1)
        else:
            return ((n - 1) * 3)



def main():
    q = iinput()
    print(q ** 3)
    
    
    


main()

