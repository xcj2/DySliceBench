import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()
    lst = [0 for _ in range(10**6+1)]
    a.sort()
    cnt = 0
    st = set()

    for i in a:
        if lst[i] == -1:
            pass
        elif lst[i] == 0:
            cnt += 1
            lst[i] = 1
            time = 10**6//i
            for j in range(2,time+1):
                lst[i*j] = -1
        elif lst[i] == 1:
            st.add(i)
    
    ans = cnt - len(st)
    print(ans)
main()            
