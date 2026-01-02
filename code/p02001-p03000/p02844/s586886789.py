#import sys
MOD = 10 ** 9 + 7
#input = sys.stdin.readline
import math

#import bisect

def sosuhante(n):
    for k in range(2, int(math.sqrt(n))+1):
        if n% k ==0:
            return False
    return True
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def kingaku(a,b,n):
    keta=len(str(n))
    return a*n+b*keta

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default


def main():
#    h,w,a,b = map(int, input().split())
#    c = [[0 for j in range(n)] for i in range(n)]
    n=int(input())
    s=list(map(str,input()))
    a=[]
    for i in range(1000):
        if i<10:
            a.append("00"+str(i))
        elif i>=10 and i<100:
            a.append("0"+str(i))
        else:
            a.append(str(i))
#    print(s)
#    print(a)
    count=0
    for i in range(1000):
        keta1=a[i][0]
        keta2=a[i][1]
        keta3=a[i][2]
   #     print(keta1,keta2,keta3)
        x=my_index(s,keta1,n+1)
        if x>=n-1:
            continue

        y = my_index(s[x+1:], keta2,n+1)
        if y>=len(s[x+1:])-1:
            continue
        z = my_index(s[x+y+2:], keta3,n+1)
        if z>len(s[x+y+2:]):
            continue
        if x!=n+1 and y!=n+1 and z!=n+1:
        #    print(s[x],s[y],s[z],i)
            count+=1
    print(count)

#  print(c)




            #    print(n,kingaku(a,b,x))

if __name__ == "__main__":
    main()