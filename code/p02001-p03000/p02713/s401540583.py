from math import gcd

############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input().rstrip()))
def inlt():
    return(list(map(int,input().rstrip().split())))
def insr():
    s = input().rstrip()
    return(s[:len(s) - 1])
def invr():
    return(map(int,input().rstrip().split()))
################################################################
n = inp()
s = 0
for i in range(1,n + 1):
    for j in range(1,n + 1):
        b = gcd(i,j)
        for k in range(1, n + 1):
            s += gcd(b,k)
print(s)
#print('No')
#print()
