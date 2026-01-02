from itertools import permutations

def check(xs):
    if xs[0] != xs[-1] ^ xs[1]:
        return False
    for i in range(1, len(xs)-1):
        if xs[i] != xs[i-1] ^ xs[i+1]:
            return False
    if xs[-1] != xs[-2] ^ xs[0]:
        return False
    return True

def solve0(A):
    for xs in permutations(A):
        if check(xs):
            return "Yes"
    return "No"

def solve(A):
    """
    N <= 10**5
    A <= 10**9
    a[i] == a[i-1] xor a[i+1]
    """
    x = 0
    for a in A:
        x ^= a

    return "Yes" if x == 0 else "No"

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    print(solve(A))

if 0==1:
    from random import randint
    N = 7
    for j in range(1, 100):
        A = [randint(0, 999999999) for i in range(N)]
        answer0 = solve0(A)
        answer = solve(A)
        if answer != answer0:
            print(answer, answer0)
            exit(1)

main()
