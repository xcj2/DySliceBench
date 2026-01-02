def compute():
  from sys import stdin
  N = int(stdin.readline().strip())
  MOD = int(1e9)+7

  dp = {}
  prohibited = ('AGC', 'ACG', 'GAC')

  def flt(a,b,c,d):
    if (b is None) or (c is None) or (d is None):
      return True
    if (b+c+d) in prohibited:
      return False
    if (a is not None) and (((a+c+d)=='AGC') or ((a+b+d)=='AGC')):
      return False
    return True

  def f(prev3, prev2, prev1, n):
    if n==0:
      return 1

    k = (prev3, prev2, prev1, n)
    if k in dp:
      return dp[k]

    nexlis = ('A', 'C', 'G', 'T')
    ret = sum(map(
      lambda nex: f(prev2, prev1, nex, n-1),
      filter(
        lambda nex: flt(prev3, prev2, prev1, nex),
        nexlis
      )
    )) % MOD

    dp[k] = ret
    return ret

  print( f(None, None, None, N) )


if __name__ == "__main__":
  compute()
