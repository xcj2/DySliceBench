#include <CodeforcesSolutions.h>
#include <ONLINE_JUDGE <solution.cf(contestID = "1362",problemID = "B",method = "GET")>.h>
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
    k = inp()
    s = insr()
    if len(s) <= k:
        print(s)
    else:
        print(s[:k] + "...")
                
################## ---- THE ACTUAL CODE ENDS ABOVE ---- ##################
##########################################################################
 
def main():
    global tt
    if not ONLINE_JUDGE:
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    t = 1
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

def power_two(n):
    if n == 1:
        return(True)
    sttr = str(n)
    len_str = len(sttr)
    sttr = list(sttr)
    num = 0
    if (len_str == 1 and sttr[len_str - 1] == '1'): 
        return(False)
    while (len_str != 1 or sttr[len_str - 1] != '1'):
        if ((ord(sttr[len_str - 1]) - ord('0')) % 2 == 1):
            return(False)
        j = 0; 
        for i in range(len_str):  
            num = num * 10 + (ord(sttr[i]) - ord('0')); 
            if (num < 2): 
                if (i != 0):  
                    sttr[j] = '0'
                    j += 1
                continue
  
            sttr[j] = chr((num // 2) + ord('0'))
            j += 1; 
            num = (num) - (num // 2) * 2
        len_str = j
    return(True)

def log_two(n): 
    return(math.log(n) / math.log(2))

#-----------------------------------------------------------------------#
        
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    input = sys.stdin.readline
    
main()