
def func(A,B):
    return max(len(str(A)),len(str(B)))

def enum_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def main():
    N = int(input())
    divisors = enum_divisors(N)
    res = float('inf')
    for i in range(len(divisors)):
        A = divisors[i]
        B = int(N/A)
        if B < A:
            break
        res = min(res,func(A,B))

    print(res)

if __name__ == "__main__":
    main()