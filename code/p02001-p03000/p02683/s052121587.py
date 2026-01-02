#include <CodeforcesSolutions.h>
#include <ONLINE_JUDGE_SOLUTION <solution.cf(contestID = "1359",problemID = "C",method = "GET")>.h>
"""
    Author : thekushalghosh
    Team   : CodeDiggers
 
    I prefer Python language over the C++ language :p :D
        
    Visit my website : thekushalghosh.github.io
"""
import sys,math,cmath,time,itertools
start_time = time.time()
##########################################################################
################# ---- THE ACTUAL CODE STARTS BELOW ---- #################

def solve():
    ONLINE_JUDGE_SOLUTION = Codeforces.CodeforcesSolutions("1361","A","GET","POST")
    print(ONLINE_JUDGE_SOLUTION)
                
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

class Codeforces():
    def CodeforcesSolutions(id,question,get,post):
        n,m,x = invr()
        a = []
        c = []
        qwqw = []
        for i in range(n):
            s = inlt()
            c.append(s.pop(0))
            a.append(s)
        q = [i for i in range(n)]
        for i in range(n):
            w = list(itertools.combinations(q,i + 1))
            for j in range(len(w)):
                qw = w[j]
                qq = [0] * m
                ww = 0
                for k in range(len(qw)):
                    ww = ww + c[qw[k] - 1]
                    qq = [qq[l] + a[qw[k] - 1][l] for l in range(m)]
                if min(qq) >= x:
                    qwqw.append(ww)
        if qwqw:
            return(min(qwqw))
        return(-1)
                    


        q = min(a,d)
        w = min(b,d - q)
        qw = min(d - q - w,c)
        return(q - qw)
        
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    input = sys.stdin.readline
    
main()