a, b, c, d = map(int, input().split())

#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

def multiple_counting(range, a, b):
    return (range -range//a -range//b +range//lcm(a,b))

def main():
    print(multiple_counting(b, c, d) - multiple_counting(a-1, c, d))

def test():
    from fractions import gcd
    A, B, C, D = map(int, input().split())
    l = C * D // gcd(C, D)
    x = (A - 1) - (A - 1) // C - (A - 1) // D + (A - 1) // l
    y = B - B // C - B // D + B // l
    print(y - x)
main()