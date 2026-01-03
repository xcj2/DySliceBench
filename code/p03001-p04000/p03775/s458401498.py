def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def F(A, B):
    return max(len(str(A)), len(str(B)))

def main():
    N = int(input())
    dvs = make_divisors(N)
    flag = False
    if len(dvs)%2 != 0:
        flag = True
        ldvs = dvs.pop()
    ans = float('inf')
    for i in range(len(dvs)//2):
        ans = min(ans, F(dvs[2*i], dvs[2*i+1]))
    if flag:
        ans = min(ans, len(str(ldvs)))
    print(ans)

if __name__ == "__main__":
    main()
