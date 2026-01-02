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
import math as mt
# sys.setrecursionlimit(10**6)

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

def printwsp(*args): return print(*args, end="")
def printsp(*args): return print(*args, end=" ")
def printchk(*args): return print(*args, end="tst, ")

MOD = int(1e9+7); BABYMOD = 998244353;
# ################################ HELPER PROGRAMS USED ###################################
# ################################## MAIN STARTS HERE #####################################
# for _testcases_ in range(int(input())):
n, k = get_ints()
count = [False]*n
for i in range(k):
    d = int(input())
    li = get_array()
    for i in li:
        count[i-1] = True
ans = 0
for i in count:
    if i is False:
        ans += 1
print(ans)

# #########################################################################################
'''
THE LOGIC AND APPROACH WAS DEVELOPED BY ME @luctivud.
SOME PARTS OF THE CODE HAS BEEN TAKEN FROM WEBSITES LIKE::
(I Own the code if no link is provided here or I may have missed mentioning it)
PLEASE DO NOT PLAGIARISE.
'''