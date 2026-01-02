#ABC141-E Who Says a Pun?
"""
ロリハ解
探索する文字列の長さを二分探索し、重複を探す。
計算量はO((n+m)*log(n//2)) ※mは探索する文字列の長さ
log部分は100には間違いなく収まるので、O(10^5)程度。十分に間に合う。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
s = readline().rstrip().decode('utf-8')

class RollingHash(): #衝突を防ぐため、res1とres2の基数の異なるハッシュによって判定する。
    BASE1 = 1007
    BASE2 = 2009
    MOD1 = 1000000007
    MOD2 = 1000000009
 
    def __init__(self, s):
        self.n = len(s)
        self.hash1 = [0] * (self.n + 1)
        self.hash2 = [0] * (self.n + 1)
        self.power1 = [1] * (self.n + 1)
        self.power2 = [1] * (self.n + 1)
        for i, e in enumerate(s):
            self.hash1[i + 1] = (self.hash1[i] * self.__class__.BASE1 + ord(e)) % self.__class__.MOD1
            self.hash2[i + 1] = (self.hash2[i] * self.__class__.BASE2 + ord(e)) % self.__class__.MOD2
            self.power1[i + 1] = (self.power1[i] * self.__class__.BASE1) % self.__class__.MOD1
            self.power2[i + 1] = (self.power2[i] * self.__class__.BASE2) % self.__class__.MOD2
 
    def get(self, l: int, r: int):
        res1 = self.hash1[r] - self.hash1[l] * self.power1[r - l] % self.__class__.MOD1
        if(res1 < 0):
            res1 += self.__class__.MOD1
        res2 = self.hash2[r] - self.hash2[l] * self.power2[r - l] % self.__class__.MOD2
        if(res2 < 0):
            res2 += self.__class__.MOD2
        return (res1, res2)


def func(mid): #ここが関数部分
    dic1 = dict()

    for i in range(n-mid+1):
        res = roliha.get(i,i+mid)
        if res in dic1:
            #部分重複があってはならない。(2つの文字列は独立)
            if i-dic1[res] >= mid: #先頭文字がmidの幅以上あるならば
                return True
            else:
                continue #更新処理を飛ばさないといけない
        dic1[res] = i
    return False 


def binary_search(): #2分探索
    ok = 0
    ng = n//2+1
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if func(mid):
            ok = mid
        else:
            ng = mid

    return ok

roliha = RollingHash(s)

print(binary_search())