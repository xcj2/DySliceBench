def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    A,B=map(int, input().split())
    ans = factorization(gcd(A,B))
    if ans[0][0] == 1:
        print(1)
    else:
        print(len(ans)+1)

if __name__ == '__main__':
    main()