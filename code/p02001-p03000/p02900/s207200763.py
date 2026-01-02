#nの素数判定
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

#nの約数列挙
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            ass.append(n//i)
    return ass #sortされていない

#nの素因数分解(O(n**0.5)
def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass


if __name__ == '__main__':
    ta, tb = map(int,input().split())

    # めんどくさいのでa<=bの場合で考える
    if ta > tb:
        a = tb
        b = ta
    else:
        a = ta
        b = tb

    a_div_set = set(divisor(a))
    b_div_set = set(divisor(b))
    common_div_set = (a_div_set & b_div_set)

    answer = 0
    for e in common_div_set:
        if e == 1 or is_prime(e):
            answer += 1
    print(answer)


