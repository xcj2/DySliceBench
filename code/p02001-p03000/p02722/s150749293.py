def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            if i**2 == n:
                continue
            ass.append(n//i)
            if i == 1:
                continue
            ass.append(i)
    ass.sort()
    return ass #sortされていない

def check(n,k):
    while n > k:
        if n % k == 0:
            n //= k
        else:
            n -= k

    if n % k == 0:
        return True
    elif n - k == 1:
        return True
    else:
        return False


def main():
    N = int(input())
    if N == 2:
        print(1)
        exit()
    div = divisor(N-1)
    ans = [N] + div
    for i in range(1,int(N**0.5)+1):
        if i in div:
            continue
        tmp = int(N)
        if i == 1:
            continue
        if N % i == 0:
            while tmp % i == 0:
                tmp //= i
            if tmp % i == 1:
                ans.append(i)
        elif N % i == 1:
            ans.append(i)
        else:
            tmp -= i + 1
            if tmp % i == 0:
                ans.append(i)
    print(len(ans))




    


if __name__ == "__main__":
    main()