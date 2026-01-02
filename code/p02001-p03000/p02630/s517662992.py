import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    suuretu = LI()
    q = I()
    dic = collections.Counter(suuretu)
    nowsum = sum(suuretu)
    
    for _ in range(q):
        b,c = LI()
        cnt = dic[b]
        nowsum += (c-b)*cnt
        print(nowsum)
        dic[b] = 0
        dic[c] += cnt
main()            
