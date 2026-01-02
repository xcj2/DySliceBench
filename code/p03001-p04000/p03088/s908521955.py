N = int(input())

# badX[n] == 条件を満たさない長さnのACGT列のうち接尾辞がXであるものの個数
bad   = [0]
badA  = [0]
badG  = [0]
badAC = [0]

def nall(n):
    """長さnのACGT列の総数"""
    return 4 ** n if n >= 0 else 0

def good(n):
    """条件を満たす長さnのACGT列の個数"""
    return nall(n) - bad[n] if n >= 0 else 0
def goodG(n):
    """条件を満たす長さnのACGT列のうち接尾辞がGであるものの個数"""
    return nall(n - 1) - badG[n] if n >= 0 else 0
def goodAC(n):
    """条件を満たす長さnのACGT列のうち接尾辞がACであるものの個数"""
    return nall(n - 2) - badAC[n] if n >= 0 else 0

for n in range(1, N + 1):
    b  = bad [n - 1] * 4              # 前半(n-1)文字が条件を満たさない
    b += good(n - 3)                  # 末尾が AGC
    b += good(n - 3) - goodG (n - 3)  # 末尾が ACG
    b += good(n - 3) - goodAC(n - 3)  # 末尾が GAC
    b += good(n - 4) * 3              # 末尾が ATGC, AGGC, AGTC
    bad.append(b)
    bA   = bad [n - 1]  # 前半(n-1)文字が条件を満たさない (+ 末尾A)
    bG   = bad [n - 1]  # 前半(n-1)文字が条件を満たさない (+ 末尾G)
    bAC  = badA[n - 1]  # 前半(n-1)文字が条件を満たさず末尾がA (+ 末尾C)
    bG  += good(n - 3) - goodG (n - 3)  # 末尾がACG
    bAC += good(n - 3) - goodAC(n - 3)  # 末尾がGAC
    badA.append(bA)
    badG.append(bG)
    badAC.append(bAC)

print(good(N) % (10 ** 9 + 7))
