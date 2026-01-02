import sys
import cmath
input = sys.stdin.buffer.readline
pi = cmath.pi
exp = cmath.exp

""" https://tjkendev.github.io/procon-library/python/fft/fft.html
"""

def make_exp_t(fn, base):
    exp_t = {0: 1}
    temp = fn
    while temp:
        exp_t[temp] = exp(base / temp)
        temp >>= 1
    return exp_t

def fft_dfs(f, s, fn, st, exp_t):
    if fn==2:
        a = f[s]; b = f[s+st]
        return [a+b, a-b]
    fn2 = fn//2; st2 = st*2
    F0 = fft_dfs(f, s   , fn2, st2, exp_t)
    F1 = fft_dfs(f, s+st, fn2, st2, exp_t)
    w = exp_t[fn]; wk = 1.0
    for k in range(fn2):
        U = F0[k]; V = wk * F1[k]
        F0[k] = U + V
        F1[k] = U - V
        wk *= w
    F0.extend(F1)
    return F0

def fft_init(n: int):
    fn = 2**(n-1).bit_length()
    fft_exp_t = make_exp_t(fn, -2j*pi)
    ifft_exp_t = make_exp_t(fn, 2j*pi)

    def fft(f):
        if fn==1: return f
        F = fft_dfs(f, 0, fn, 1, fft_exp_t)
        return F

    def ifft(F):
        if fn==1: return F
        f = fft_dfs(F, 0, fn, 1, ifft_exp_t)
        f = [x/fn for x in f]
        return f

    return fn, fft, ifft

def pad(f, fn):
    return f + [0,]*max(0, fn-len(f))

def roll(f, shift):
    return f[-shift:] + f[:-shift]

def main():
    N, M = map(int, input().split())
    vA = list(map(int, input().split()))
    nH = 10**5 + 1
    vH = [0,]*nH
    for a in vA:
        vH[a] += 1

    fn, fft, ifft = fft_init(nH*2)
    vH = pad(vH, fn)
    #vB = pad(vB, fn)
    vB = roll(vH, 1)

    fA = fft(vH)
    fB = fft(vB)
    fC = [a*b for a,b in zip(fA,fB)]
    vC = ifft(fC)
    rC = [int(x.real+.5) for x in vC]
    print(*rC[50:70], sep=" ", file=sys.stderr)

    res = 0
    for i,c in zip(reversed(range(len(rC))),rC[::-1]):
        if M>=c:
            res += (i-1)*c
            M -= c
        else:
            res += (i-1)*M
            break
    print(res)

if __name__ == "__main__":
    main()
