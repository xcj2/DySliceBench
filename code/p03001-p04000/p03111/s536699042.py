#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list
#from itertools import combinations # (string,3) 3回
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    n,A,B,C = readInts()
    L = [] * n
    for i in range(n):
        l = int(input())
        L.append(l)

    def rec(i,a,b,c):
        if i == n:
            if not a or not b or not c:
                return float('inf')
            return abs(a-A) + abs(b-B) + abs(c - C)
            # 一番最後まで行ったら、その差が延長魔法や短縮魔法を使うMPであるからこうする

        # 今ある竹を採用しない場合
        res = rec(i+1, a, b, c)

        # A,B,Cを使う場合 (どこにどれを足す？)
        # 1本目はコストなし、2本目からコスト10
        res = min(res,rec(i+1,a+L[i],b,c) + (10 if a >= 1 else 0)) # aにL[i]を足す
        res = min(res,rec(i+1,a,b+L[i],c) + (10 if b >= 1 else 0)) # bにL[i]を足す
        res = min(res,rec(i+1,a,b,c+L[i]) + (10 if c >= 1 else 0)) # cにL[i]を足す
        return res

    print(rec(0,0,0,0))


if __name__ == '__main__':
  main()
