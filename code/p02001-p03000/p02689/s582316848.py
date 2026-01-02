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
n, m = get_ints()
height = get_array()
ansli = [True] * n
for _ in range(m):
    a, b = get_ints()
    a-=1; b-=1;
    if height[a] > height[b]:
        ansli[b] = False
    elif height[a] < height[b]:
        ansli[a] = False
    elif height[a] == height[b]:
        ansli[a] = False
        ansli[b] = False
ans = 0
for i in ansli:
    if i:
        ans += 1
print(ans)


# #########################################################################################
'''
THE LOGIC AND APPROACH WAS DEVELOPED BY ME @luctivud.
SOME PARTS OF THE CODE HAS BEEN TAKEN FROM WEBSITES LIKE::
(I Own the code if no link is provided here or I may have missed mentioning it)
PLEASE DO NOT PLAGIARISE.
'''