import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


def z_algorithm(s):
    n = len(s)
    z = [0]*n
    z[0] = n
    i = 1
    j = 0
    while i<n:
        while i+j<n and s[j]==s[i+j]:
            j+=1
        z[i] = j

        if j==0:
            i+=1
            continue

        k = 1
        while k+z[k]<j:
            z[i+k] = z[k]
            k+=1
        
        i+=k
        j-=k
    
    return z

n = readint()
s = readstr()

ans = 0
for i in range(n):
    z = z_algorithm(s[i:])
    for j in range(n-i):
        if z[j]<=j:
            ans = max(ans,z[j])
print(ans)




