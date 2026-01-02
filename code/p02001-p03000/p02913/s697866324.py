import sys,collections as cl,bisect as bs,heapq as hq
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

def search(a,n):
    se = dict()
    data = []
    for i in range(0,len(a)-n+1):
        kkk = a[i:i+n]
        kkk = "".join(kkk)
        if In(kkk,data):
            if se[kkk] <= i-n:
                    return True
        else:
            bs.insort(data,kkk)
            se[kkk] = i
    return False
def solver():
    n = onem()

    s = list(input())
    l = 0
    r = n//2
    for i in range(n):
        mid = -(-(l+r)//2)
        ans = search(s,mid)
        if l == mid:
            break
        if ans:
            l = mid
        else:
            r = mid-1
    print(l)



if __name__ == '__main__':
    solver()


