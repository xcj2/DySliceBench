import itertools

def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    A, B = map(int, input().split())

    div_A = divisor(A)
    div_B = divisor(B)
    C = list(set(div_A) & set(div_B))
    cnt = 1
    for c in C:
        if is_prime(c):
            cnt += 1

    print(cnt)

main()