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

a = LIR(3)
n = I()
b = IR(n)


def check(A, B):
   S = set(b)
 
   # check each row
   for r in range(3):
      cnt = 0
      for c in range(3):
         if A[r][c] in S:
            cnt += 1
      if cnt == 3:
         return True
 
   # check each colum
   for c in range(3):
      cnt = 0
      for r in range(3):
         if A[r][c] in S:
            cnt += 1
      if cnt == 3:
         return True
 
   # check back diagonal
   cnt = 0
   for i in range(3):
      if A[i][i] in S:
         cnt += 1
   if cnt == 3:
      return True
 
   # check forward diagonal
   cnt = 0
   for i in range(3):
      if A[i][2-i] in S:
         cnt += 1
   if cnt == 3:
      return True
 
   return False
 
 
print('Yes' if check(a, b) else 'No')
