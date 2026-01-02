# -*- coding: utf-8 -*-

import numpy as np

EDPC = "https://atcoder.jp/contests/dp/"
TDPC = "https://atcoder.jp/contests/tdpc/tasks"

################ DANGER ################
test = ""
#test = \
"""
5 3
10 30 40 50 20
ans 30
0 20 30 40 30
"""

"""
3 1
10 20 10
ans 20
"""

"""
2 100
10 10
ans 0
"""

"""
10 4
40 10 20 70 80 10 20 70 80 60
ans 40
0 30 20 30 40 30 20 30 40 40
"""
########################################
test = list(reversed(test.strip().splitlines()))
if test:
    def input2():
        return test.pop()
else:
    def input2():
        return input()
########################################  

n, k = map(int, input2().split())
a = list(map(int, input2().split()))
k = min(n-1, k)

def main(n, k, a):
    aa = np.concatenate([a])
    dp = np.concatenate([np.abs(aa - aa[0])[:k+1], 
                                np.zeros(n-k-1, dtype="int")])
    for i in range(k+1, n):
        dp[i] = np.min(dp[i-k:i] + np.abs(aa[i-k:i] - aa[i]))
    
    return dp[-1]


if __name__ == "__main__":
    print(main(n, k, a))
