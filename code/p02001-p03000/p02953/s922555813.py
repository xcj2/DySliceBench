import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools, os
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)
def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('- {} -> {}'.format(name, val), file=sys.stderr)
            return None

def main(N, H):
    """
    一番右の数字は低くする義理がない
    逆から見る？
    """
    for hidx in range(N):
        if hidx == 0:
            continue
        
        if H[N-1-hidx] > H[N-1-hidx+1]:
            H[N-1-hidx] -= 1
            if H[N-1-hidx] > H[N-1-hidx+1]:
                return 'No'
    else:
        for hidx in range(N-1):
            if H[hidx] > H[hidx+1]:
                return 'No'
        else:
            return 'Yes'



    #  for hidx in range(N-1):
    #      #  print(H)
    #      if H[hidx] > H[hidx+1]:
    #          # 左のもののほうが高い場合
    #          H[hidx] -= 1
    #          if H[hidx] > H[hidx+1]:
    #              # それでもまだ高い場合
    #              return 'No'
    #  else:
    #      for hidx in range(N-1):
    #          if H[hidx] > H[hidx+1]:
    #              return 'No'
    #      else:
    #          return 'Yes'


if __name__ == '__main__':
    if 'LOCAL' in os.environ:
        # ローカル実行時のみ通る処理
        # テストしたい入力を入れておく
        input_values = [
                """
                """.strip(),
                """
                """.strip()
                ]
        for input_value in input_values:
            input_value = input_value.split('\n')
            #  N = int(input_value[0])
            #  A = list(map(int, input_value[1].split()))
            ans = main(N, A)
            expected_value = int(input_value[2])
            assert ans == expected_value, 'failed: ans: {ans}, exp: {exp}'.format(ans=ans, exp=expected_value)
    else:
        N = _I()
        H = LI()
        print(main(N, H))


