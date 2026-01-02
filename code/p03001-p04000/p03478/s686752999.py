def readinput():
    n,a,b = list(map(int,input().split()))
    return n,a,b

def sumdigit(n):
    sum=0
    t = getdigits(n)
    #print(n, t)
    for n in t:
        sum+=n
    return sum

def getdigits(n):
    if (n==10000):
        return (1,0,0,0,0)
    
    d4 = n // 1000
    n -= d4*1000
    d3 = n // 100
    n -= d3*100
    d2 = n // 10
    n -= d2*10
    return (d4,d3,d2,n)

def main(n,a,b):
    sum=0
    for i in range(1,n+1):
        s = sumdigit(i)
        #print(s)
        if (a<=s and s<= b):
            sum += i
    return sum

if __name__ == '__main__':
    n,a,b = readinput()
    sum = main(n,a,b)
    print(sum)