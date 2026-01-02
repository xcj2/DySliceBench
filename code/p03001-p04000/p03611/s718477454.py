import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()
    dic = collections.defaultdict(int)
    for i in a:
        for x in range(i-1,i+2):
            dic[x] += 1
    diclst = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    ans = diclst[0][1]
    print(ans)
main()