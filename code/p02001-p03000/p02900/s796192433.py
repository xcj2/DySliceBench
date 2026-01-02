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
    div_A = set(divisor(A))
    div_B = set(divisor(B))
    div_list = list(div_A & div_B)
    cnt = 1
    for n in div_list:
        if is_prime(n):
            cnt += 1

    print(cnt)



if __name__ == "__main__":
    main()