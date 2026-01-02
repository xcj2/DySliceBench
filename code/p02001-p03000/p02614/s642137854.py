"""
    こんにちは。これはクシャルです
    
    Author : thekushalghosh (クシャル)
    Team   : CodeDiggers
 
    I prefer Python language over the C++ language :p :D
        
    Visit my website : thekushalghosh.github.io
"""
import sys,math,cmath,time,itertools
start_time = time.time()
##########################################################################
################# ---- THE ACTUAL CODE STARTS BELOW ---- #################

def solve():
    h,w,k = invr()
    a = []
    qq = [i + 1 for i in range(h)]
    ww = [i + 1 for i in range(w)]
    for i in range(h):
        s = insr()
        a.append(s)
    r = [0] * h
    c = [0] * w
    b = transpose(a)
    qwqw = 0
    for i in range(h):
        r[i] = a[i].count("#")
    for i in range(w):
        c[i] = b[i].count("#")
    qqww = sum(r)
    for i in range(7):
        q = list(itertools.combinations(qq,i))
        for j in range(len(q)):
            for ii in range(7):
                w = list(itertools.combinations(ww,ii))
                for jj in range(len(w)):
                    qw = 0
                    for ij in range(i):
                        qw = qw + r[q[j][ij] - 1]
                    for ij in range(ii):
                        qw = qw + c[w[jj][ij] - 1]
                    for ij in range(i):
                        for ijij in range(ii):
                            if a[q[j][ij] - 1][w[jj][ijij] - 1] == "#":
                                qw = qw - 1
                    if qqww - qw == k:
                        qwqw = qwqw + 1
    print(qwqw)
    
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

def counter_elements(a):
    q = dict()
    for i in range(len(a)):
        if a[i] not in q:
            q[a[i]] = 0
        q[a[i]] = q[a[i]] + 1
    return(q)

def string_counter(a):
    q = [0] * 26
    for i in range(len(a)):
        q[ord(a[i]) - 97] = q[ord(a[i]) - 97],1
    return(q)
 
def factors(n):
    q = []
    for i in range(1,int(n ** 0.5) + 1):
        if n % i == 0: q.append(i); q.append(n // i)
    return(list(sorted(list(set(q)))))
 
def prime_factors(n):
    q = []
    while n % 2 == 0: q.append(2); n = n // 2
    for i in range(3,int(n ** 0.5) + 1,2):
        while n % i == 0: q.append(i); n = n // i
    if n > 2: q.append(n)
    return(list(sorted(q)))

def transpose(a):
    n,m = len(a),len(a[0])
    b = [[0] * n for i in range(m)]
    for i in range(m): 
        for j in range(n): 
            b[i][j] = a[j][i]
    return(b)

#-----------------------------------------------------------------------#
        
ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    input = sys.stdin.readline
    
    
main()