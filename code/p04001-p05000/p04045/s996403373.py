import sys
input = sys.stdin.readline
import math

def INT(): return int(input())
def MAPINT(): return map(int, input().split())
def LMAPINT(): return list(map(int, input().split()))
def STR(): return input()
def MAPSTR(): return map(str, input().split())
def LMAPSTR(): return list(map(str, input().split()))

f_inf = float('inf')


def main():

    N, K = MAPINT()
    D = LMAPSTR()
    
    str_n = str(N)
    
    for i in range(N, 100000):
      str_i = str(i)
      for s in str_i:
        if s in D:
          break
      else:
        print(str_i)
        exit()

        
if __name__ == "__main__":
    main()
