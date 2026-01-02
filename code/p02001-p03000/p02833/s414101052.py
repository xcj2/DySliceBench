
def f0(N):
    if N < 2:
        return 1
    return N * f0(N-2)

def f(N):
    answer = 1
    n = N
    while n >= 2:
        answer *= n
        n -= 2
    return answer

def test(N):
    b = f(N)
    answer = 0
    while b > 0:
        b, r = divmod(b, 10)
        if r == 0:
            answer += 1
        else:
            break
    return answer

def solve(N):
    M = 10**18
    a = 10
    A = []
    while a <= M:
        A.append(a)
        a *= 5
    #print(len(A))

    if N % 2 == 1:
        return 0
    answer = 0
    for a in A:
        answer += N//a
    return answer

"""
for i in (98, 100, 110, 120, 148, 150, 200, 248, 250, 296, 298, 300, 400, 900, 950, 1000, 5000, 100000):
    t = test(i)
    print(i, t, solve(i), i//10, i//50, i//250, "rem:%d"%(t-(i//10+i//50+i//250+i//(5**3*10))), sep="\t")
"""
N = int(input())
print(solve(N))
