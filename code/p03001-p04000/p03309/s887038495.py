memo={}
def calc(A, b):
    score = memo.get(b, None)
    if not score is None:
        return score
    score = sum(abs(a-b) for a in A)
    memo[b] = score
    return score

c = 0
def findmin(A, l, u):
    global c
    c+=1
    d = (u-l)//3
    if d == 0:
        return min(calc(A, i) for i in range(l, u+1))
    left, right = l + d, u - d
    sl = calc(A, left) 
    sr = calc(A, right) 
    if sl > sr:
        return findmin(A, left, u)
    else:
        return findmin(A, l, right)

def solve(A):
    B= [0] * len(A)
    l = A[0]
    u = A[0]
    for i, a in enumerate(A):
        b = a-(i+1)
        l = min(l, b)
        u = max(u, b)
        B[i] = b
    #A = [a-(i+1) for i, a in enumerate(A)]
    return findmin(B, l, u)

N = int(input())
A = [int(x) for x in input().split()]

#abs(A1-(b+1)) + abs(Ai-(b-i)) + abs(AN-(b-N))


# b1 = A[0]    ならば (A[i]-b1) >= 0
# b2 = A[0] -1 ならば (A[i]-b2) > (A[i]-b1) >= 0 なので、スコアは大きくなる

# b = A[-1] ならば (A[i]-b) <= 0
print(solve(A))

