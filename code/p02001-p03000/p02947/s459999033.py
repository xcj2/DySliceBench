import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n = I()
    lst = []
    for _ in range(n):
        st = S()
        st = list(st)
        st.sort()
        lst.append("".join(st))

    ans = 0
    dic = collections.Counter(lst)
    for key,value in dic.items():
        if value >= 2:
            ans += value*(value-1)//2
    print(ans)
main()