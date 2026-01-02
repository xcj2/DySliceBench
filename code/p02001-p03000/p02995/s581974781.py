#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)
def main():
    A, B, C, D = [int(n) for n in input().split()]
    min_c = A // C if A % C == 0 else (A // C)+1
    max_c = B // C if B % C == 0 else (B // C)
    min_d = A // D if A % D == 0 else (A // D)+1
    max_d = B // D if B % D == 0 else (B // D)
    pro = lcm(C, D)
    min_pro = A // (pro) if A % (C*D) == 0 else (A // (pro))+1
    max_pro = B // (pro) if B % (C*D) == 0 else (B // (pro))
    

    print((B-A+1) - (max_c-min_c+1) - (max_d-min_d+1) + (max_pro-min_pro + 1))
main()

