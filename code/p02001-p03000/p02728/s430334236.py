from functools import reduce

def extended_euclid(a, b):
    x1, y1, m = 1, 0, a
    x2, y2, n = 0, 1, b
    while m % n != 0:
        q, r = divmod(m, n)
        x1, y1, m, x2, y2, n = x2, y2, n, x1 - q * x2, y1 - q * y2, r
    return x2, y2, n

def modular_inverse(a, mod):
    x, _, g = extended_euclid(a, mod)
    if g != 1:
        return None # Modular inverse of a does not exist
    else:
        return x % mod

class Combinatorics:
    def __init__(self, N, mod):
        '''
        Preprocess for calculating binomial coefficients nCr (0 <= r <= n, 0 <= n <= N)
        over the finite field Z/(mod)Z.
        Input:
            N (int): maximum n
            mod (int): a prime number. The order of the field Z/(mod)Z over which nCr is calculated.
        '''
        self.mod = mod
        self.fact = [0] * (N+1)           # n!
        self.inverse = [None] + [0] * N   # inverse of n in the field Z/(MOD)Z
        self.fact_inverse = [0] * (N+1)   # inverse of n! in the field Z/(MOD)Z
        
        # preprocess
        self.fact[0] = self.fact[1] = 1
        self.fact_inverse[0] = self.fact_inverse[1] = 1
        self.inverse[1] = 1
        for i in range(2, N+1):
            self.fact[i] = i * self.fact[i-1] % self.mod
            q, r = divmod(self.mod, i)
            self.inverse[i] = (- (q % self.mod) * self.inverse[r]) % self.mod
            self.fact_inverse[i] = self.inverse[i] * self.fact_inverse[i-1] % self.mod
    
    def perm(self, n, r):
        '''
        Calculate nPr = n! / (n-r)! % mod
        '''
        if n < r or n < 0 or r < 0: return 0
        else: return (self.fact[n] * self.fact_inverse[n-r]) % self.mod
    
    def binom(self, n, r):
        '''
        Calculate nCr = n! /(r! (n-r)!) % mod
        '''
        if n < r or n < 0 or r < 0: return 0
        else: return self.fact[n] * (self.fact_inverse[r] * self.fact_inverse[n-r] % self.mod) % self.mod
        
    def multinom(self, R):
        '''
        Calculate \binom{sum(R)}{r1, ..., r_k}
        '''
        n = sum(R)
        return self.fact[n] * reduce(lambda x, y: self.fact_inverse[x] * self.fact_inverse[y] % self.mod, R) % self.mod
        
    def hom(self, n, r):
        '''
        Calculate nHr = {n+r-1}Cr % mod.
        Assign r objects to one of n classes.
        Arrangement of r circles and n-1 partitions:
            o o o | o o | | | o | | | o o | | o
        '''
        if n == 0 and r > 0: return 0
        if n >= 0 and r == 0: return 1
        return self.binom(n + r - 1, r)

MOD = 10**9 + 7
N = int(input())
com = Combinatorics(N, MOD)
T = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    T[a-1].append(b-1); T[b-1].append(a-1)

# Consider T to be rooted at r = 0
downward = [1] * N
upward = [1] * N
n_descs = [1] * N
children_n_descs = [[] for _ in range(N)]
ans = [-1] * N

def dfs1(r):
    stack = [(r, -1, 0)] # (vertex, parent, status)
    while stack:
        v, p, st = stack.pop()
        if st == 0: # visited v for the first time
            n_children = 0
            for u in T[v]:
                if u == p: continue
                if n_children == 0:
                    stack += [(v, p, 2), (u, v, 0)]
                    n_children += 1
                else:
                    stack += [(v, p, 1), (u, v, 0)]
                    n_children += 1
            if n_children == 0: # v is a leaf
                stack += [(v, p, 2)]
        elif st == 1: # now searching
            continue
        else: # search finished
            n = n_descs[v]
            downward[v] = (downward[v] * com.fact[n-1]) % MOD
            if p != -1:
                n_descs[p] += n
                downward[p] = ((downward[p] * downward[v]) % MOD * com.fact_inverse[n]) % MOD

def dfs2(r):
    f_n1, f_n1_inv = com.fact[N-1], com.fact_inverse[N-1]
    stack = [(r, -1)] # (vertex, parent)
    while stack:
        v, p = stack.pop()
        n_v = n_descs[v]
        dw_v = downward[v]
        if p == -1: upward[v] = 1
        else: upward[v] = ans[p] * com.fact[N-1-n_v] % MOD * com.fact[n_v] % MOD * modular_inverse(dw_v, MOD) % MOD * f_n1_inv % MOD
        ans[v] = upward[v] * downward[v] % MOD * f_n1 % MOD * com.fact_inverse[N-n_v] % MOD * com.fact_inverse[n_v-1] % MOD
        for u in T[v]:
            if u == p: continue
            stack += [(u, v)]
dfs1(0)
dfs2(0)
for a in ans: print(a)