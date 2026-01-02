import sys
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7

k, n = LI()
a = LI()

# 一周kメートルの円形湖があり、n軒の家がある。
# i番目のいえは北端から時計回りにAメートルのところにある。
# いずれかの家から出発してn件すべての家に尋ねるための最短移動距離を求めよ

# 円形で考えるからややこしい
# 一番距離が長い家と家の区間を除外した直線状と考えればよいのでは。

far = []

for i in range(0,n):
    if i == 0:
        d = a[0] + k - a[-1]        
    else:
        d = a[i] - a[i-1]

    far.append(d)

longest = 0

for i in range(n):
    if far[i] > longest:
        longest = far[i]
        longest_i = i
del far[longest_i]
print(sum(far))