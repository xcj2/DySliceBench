import sys
import collections
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    n = I()
    mylist = list(MI())
    max_a = max(mylist)
    exclude_set = set()
    tlist = [False] * (max_a+1)
    for a in mylist:
        if tlist[a]:
            exclude_set.add(a)
        else:
            tlist[a] = True
    ans = 0
    
    for i in range(1, max_a//2 + 1):
        if not tlist[i]:
            continue
        else:
            for j in range(2*i, max_a+1, i):
                tlist[j]=False
    for i in range(len(tlist)):
        if tlist[i] and not i in exclude_set:
            ans += 1
    print(ans)
                
    

if __name__ == '__main__':
    main()
