# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
#      .      '                    Udit Gupta @luctivud         ,              
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            ##     ##  #######  # #  ######
                            ##     ##  ##   ##  ###    ##
                            ##     ##  ##    #  # #    ##
                            #########  #######  # #    ##
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sys
import math
# sys.setrecursionlimit(10**6)

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def printwsp(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")
def printchk(*args): return print(*args, end="tst, ")

MODPRIME = int(1e9+7); BABYMOD = 998244353;
# ################################ HELPER PROGRAMS USED ###################################
# ################################## MAIN STARTS HERE #####################################
# for _testcases_ in range(int(input())):
k, n = get_ints()
a = get_array()
a.sort()
maxdiff = - float('inf')
for i in range(n-1):
    maxdiff = max(maxdiff, abs(a[i] - a[(i+1)%n]))
maxdiff = max(maxdiff, k - a[-1] + a[0])
print(k - maxdiff)

# #########################################################################################
'''
THE LOGIC AND APPROACH IS BY ME @luctivud.
SOME PARTS OF THE CODE HAS BEEN TAKEN FROM WEBSITES LIKE::
(I Own the code if no link is provided here or I may have missed mentioning it)
: DO NOT PLAGIARISE.
'''