import sys
from functools import reduce
from operator import xor
readline = sys.stdin.readline

def rev(x, k):
    res = 0
    for cnt in range(k):
        res = (res<<1) + (1&(x>>cnt))
    return res
        
class GE():
    #mod2　なら　Aは1重リストで渡して, max(bit_length) をMに渡してあげた方が速い
    def __init__(self, A, mod, M = 0):
        self.N = len(A)
        if M:
            self.M = M
        else:
            self.M = len(A[0])
        self.mod = mod
        self.A = A[:]
        self.uptri = None
        self.A2 = None
        self.pivot = []
        self.R = None
    def ut(self):
        if self.mod != 2:
            if self.uptri is not None:
                return self.uptri
            self.uptri = self.A[:]
            c = 0
            for i in range(self.N):
                if i + c >= self.M:
                    break
                while self.uptri[i][i+c] == 0:
                    for j in range(i+1, self.N):
                        if self.uptri[j][i+c]:
                            self.uptri[i], self.uptri[j] = self.uptri[j], self.uptri[i]
                            break
                    else:
                        c += 1
                        if i + c == self.M:
                            break
                else:
                    self.pivot.append((i, i+c))
                    t = pow(self.uptri[i][i+c], self.mod - 2, self.mod)
                    for j in range(i+1, self.N):
                        tj = t * self.uptri[j][i+c]
                        self.uptri[j][i+c:] = [(aj - tj*ai) % self.mod for ai, aj in zip(self.uptri[i][i+c:], self.uptri[j][i+c:])]
                    continue
                break
            for pi, pj in self.pivot[::-1]:
                t = pow(self.uptri[pi][pj], self.mod-2, self.mod)
                self.uptri[pi][pj:] = [(ai * t) % self.mod for ai in self.uptri[pi][pj:]]
                for i in range(pi-1, -1, -1):
                    ti = self.uptri[i][pj]
                    self.uptri[i][pj:] = [(ai - api*ti) % self.mod for ai, api in zip(self.uptri[i][pj:], self.uptri[pi][pj:])]
            
            return self.uptri
        else:
            if self.A2 is not None:
                return self.A2
            self.A2 = self.A[:]
            c = 0
            for i in range(self.N):
                if i + c >= self.M:
                    break
                while not self.A2[i] & 2**(i+c):
                    for j in range(i+1, self.N):
                        if self.A2[j] & 2**(i+c):
                            self.A2[i], self.A2[j] = self.A2[j], self.A2[i]
                            break
                    else:
                        c += 1
                        if i + c == self.M:
                            break
                else:
                    self.pivot.append((i, i+c))
                    for j in range(i+1, self.N):
                        if self.A2[j] & 2**(i+c):
                            self.A2[j] ^= self.A2[i]
                    continue
                break
            for pi, pj in self.pivot[::-1]:
                for i in range(pi-1, -1, -1):
                    if 2**pj & self.A2[i]:
                        self.A2[i] ^= self.A2[pi]
            
            return self.A2
            
                
    def rank(self):
        if self.R is not None:
            return self.R
        self.ut()
        self.R = len(self.pivot)
        return self.R
    
    def solve(self):
        self.ut()

N = int(readline())
A = list(map(int, readline().split()))
M = reduce(xor, A)
ans = M
k = max(A).bit_length()
T = GE([rev(a&(~M), k) for a in A], 2, 60)
print(ans + 2*(reduce(xor, [rev(x, k) for x in T.ut()])))
