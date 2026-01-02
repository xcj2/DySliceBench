from cmath import pi, exp

def convolve(a, b):
    """配列a, bの畳み込みをFFT(fast Fourier transform)によって計算する
    res[k] = sum{i=0...n}a[i]*b[k-i]
    """
    def fft(a, inverse=False):
        # バタフライ演算用の配置入れ替え
        for i in range(n):
            j = 0
            for k in range(h):
                j |= (i >> k & 1) << (h - 1 - k)
            if i < j:
                a[i], a[j] = a[j], a[i]
 
        # バタフライ演算
        sign = 1.0 if inverse else -1.0
        b = 1
        while b < n:
            for j in range(b):
                w = exp(sign * 2.0j * pi / (2.0 * b) * j)
                for k in range(0, n, b*2):
                    s = a[j + k]
                    t = a[j + k + b] * w
                    a[j + k] = s + t
                    a[j + k + b] = s - t
            b *= 2
 
        # 逆変換時には配列のサイズで割る
        if inverse:
            for i in range(n):
                a[i] /= n
        return a
 
    def ifft(a):
        return fft(a, inverse=True)
 
    n = 1 << (len(a) + len(b) - 1).bit_length()
    h = n.bit_length() - 1
    a += [0] * (n - len(a))
    b += [0] * (n - len(b))
    
    # in-placeで計算を進めることに注意
    fft(a), fft(b)
    for i in range(n):
        a[i] *= b[i]
    ifft(a)
 
    res = [int(abs(v) + 0.5) for i, v in enumerate(a)]
    return res[1:]

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a = list(map(int, input().split()))
 
cnt = [0] * (100001)
for i in a:
    cnt[i] += 1 

c = convolve(cnt[0:], cnt[0:])
ans = 0
for i in range(len(c))[::-1]:
    if c[i] > 0:
      p = min(m,c[i])
      m -= p
      ans += i*p+p
      if m == 0:
        break
print(ans)