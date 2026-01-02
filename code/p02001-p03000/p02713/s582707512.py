"""
    Author : thekushalghosh
    Team   : CodeDiggers
"""
import sys,math,cmath,time
start_time = time.time()
################# ---- USER DEFINED INPUT FUNCTIONS ---- #################
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(s[:len(s) - 1])
def invr():
    return(map(int,input().split()))
##########################################################################
################# ---- THE ACTUAL CODE STARTS BELOW ---- #################

def solve():
    n = inp()
    c = 0
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            for k in range(1,n + 1):
                c = c + math.gcd(math.gcd(i,j),k)
    print(c)
################## ---- THE ACTUAL CODE ENDS ABOVE ---- ##################
##########################################################################
ONLINE_JUDGE = __debug__
if not ONLINE_JUDGE:
    sys.stdin = open('input.txt','r')
    sys.stdout = open('output.txt','w')
else:
    input = sys.stdin.readline
t = 1
for tt in range(t):
    solve()
if not ONLINE_JUDGE:
    print("Time Elapsed:",time.time() - start_time,"seconds")
sys.stdout.close()