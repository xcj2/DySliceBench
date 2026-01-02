import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():

    n, x, m = LI()
    start = -1
    goal = -1
    a = [0 for _ in range(m+2)]
    acc = [0 for _ in range(m+2)]
    st = {x}
    a[0] = -1
    a[1], acc[1] = x, x
    for i in range(1,m+1):
        a[i+1] = a[i]**2%m
        acc[i+1] = acc[i] + a[i+1]
        if a[i+1] in st:
            start = a.index(a[i+1])
            goal = i
            break
        else:
            st.add(a[i+1])

    ans = 0
    if n<=goal:
        ans = acc[n]
    else:
        ans = acc[goal] + (acc[goal]-acc[start-1])*((n-goal)//(goal-start+1)) + acc[(n-goal)%(goal-start+1)+start-1] - acc[start-1]

    print(ans)
main()
