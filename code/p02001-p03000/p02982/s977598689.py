import math;

def swap(a,b):
    return (b,a)

def gcd(a,b):
    if (a<b):
        a,b = swap(a,b)
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

def main():
    n,d = map(int,input().split())
    x = []
    for i in range(n):
        x.append([y for y in map(int,input().split())])
    ans = 0
    for i in range(n):
        for j in range(n):
            if i>=j:
                continue
            res = 0
            for k in range(d):
                res += (x[i][k] - x[j][k]) * (x[i][k] - x[j][k])
            res = math.sqrt(res)
            res1 = int(res)
            if res1==res:
                ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()