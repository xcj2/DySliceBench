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

def main():
    return


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
            ans = main()
            expected_value = int(input_value[2])
            assert ans == expected_value, 'failed: ans: {ans}, exp: {exp}'.format(ans=ans, exp=expected_value)
    else:
        A, B, C = LI()
        ans = C- (A-B)
        if ans < 0:
            ans = 0
        print(ans)
        #  print(main())

