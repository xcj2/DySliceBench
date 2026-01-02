import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    dic = collections.defaultdict(list)
    for i in range(n):
        s, p = LS()
        p = int(p)

        dic[s].append((p,i+1))
    
    key = list(dic.keys())
    key.sort()
    for k in key:
        lst = dic[k]
        lst.sort(reverse=True)
        lst = list(zip(*lst))[1]
        for s in lst:
            print(s)

    
    
main()
