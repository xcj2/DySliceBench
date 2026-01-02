#include <CodeforcesSolutions.h>
#include <ONLINE_JUDGE <solution.cf(contestID = "1360",problemID = "F",method = "GET")>.h>
"""
    Author : thekushalghosh
    Team   : CodeDiggers
 
    I prefer Python language over the C++ language :p :D
        
    Visit my website : thekushalghosh.github.io
"""
import sys,math,cmath,time
start_time = time.time()
##########################################################################
################# ---- THE ACTUAL CODE STARTS BELOW ---- #################
    
def solve():
    n,a,b,c,d = invr()
    memo = {}
    def qw(n):
        if n == 0:
            return 0
 
        if n == 1:
            return d
 
        if n in memo:
            return memo[n]
 
        ret = n * d
 
        if (n % 2 == 0):
            ret = min(ret, a + qw(n // 2))
        else:
            ret = min(ret, (n%2)*d + a + qw(n // 2), (2-n%2)*d + a + qw((n+(2-n%2))//2))
 
        if (n % 3 == 0):
            ret = min(ret, b + qw(n // 3))
        else:
            ret = min(ret, (n%3)*d + b + qw(n // 3), (3-n%3)*d + b + qw((n+(3-n%3))//3))
 
        if (n % 5 == 0):
            ret = min(ret, c + qw(n // 5))
        else:
            ret = min(ret, (n%5)*d + c + qw(n // 5), (5-n%5)*d + c + qw((n+(5-n%5))//5))
        memo[n] = ret
        return ret
    print(qw(n))
        
################## ---- THE ACTUAL CODE ENDS ABOVE ---- ##################
##########################################################################

def main():
    global tt
    if not ONLINE_JUDGE:
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    t = 1
    t = inp()
    for tt in range(t):
        solve()
    if not ONLINE_JUDGE:
        print("Time Elapsed :",time.time() - start_time,"seconds")
    sys.stdout.close()
#---------------------- USER DEFINED INPUT FUNCTIONS ----------------------#
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    return(input().strip())
def invr():
    return(map(int,input().split()))
#------------------ USER DEFINED PROGRAMMING FUNCTIONS ------------------#
def counter(a):
    q = [0] * max(a)
    for i in range(len(a)):
        q[a[i] - 1] = q[a[i] - 1] + 1
    return(q)
 
def string_counter(a):
    q = [0] * 26
    for i in range(len(a)):
        q[ord(a[i]) - 97] = q[ord(a[i]) - 97] + 1
    return(q)
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    input = sys.stdin.readline
    
main()