import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    sys.setrecursionlimit(10**5)
    n = I()
    s = S()
    global cnt
    cnt = 0
    def tansaku(st,depth):
        global cnt
        for i in range(10):
            index = st.find(str(i))
            if index != -1:
                if depth == 0:
                    cnt += 1
                    # print(i)
                # print(st,i,index,depth)
                else:
                    tansaku(st[index+1:],depth-1)
    tansaku(s,2)

    print(cnt)

main()