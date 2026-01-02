import statistics
import sys
import math
INPUT = sys.stdin.readline
#入力関数
def SORO_INT(): return int(INPUT())
def MULT_INT_LIST(): return list(map(int, INPUT().split()))
def MULT_INT_MAP(): return map(int, INPUT().split())
def SORO_STRING(): return INPUT()
def MULT_STRING(): return INPUT().split()

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False
    
A = MULT_INT_LIST()
mean = statistics.mean(A)

if is_integer_num(mean):
  print(int(mean))
else:
  print('IMPOSSIBLE')


