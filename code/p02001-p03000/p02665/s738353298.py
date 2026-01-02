from sys import stdin
from collections import deque
def I(): return int(stdin.readline().rstrip())
def LI(): return list(map(int,stdin.readline().rstrip().split()))
 
def end():
    print(-1)
    exit()
 
def main():
    n = I()
    a = deque(LI())
    if n==0:
        if a[0] == 1:
            print(1)
            exit()
        else:
            end()
    elif a[0]!=0:
        end()

    b = [0]*(n+1)
    for i in range(n,-1,-1):
        if i == n:
            b[i] = a[i]
        else:
            b[i] = min(b[i+1]+a[i],2**i)

    for i in range(n+1):
        if i!=0:
            b[i] = min(2*(b[i-1]-a[i-1]),b[i])
        if b[i]<a[i]:
            end()
    print(sum(b))
    return
 
if __name__=='__main__':
    main()