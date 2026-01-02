def gcd_(a, b):
    if a < b:  a, b = b, a
    if b == 0:  return a
    return gcd_(b, a % b)

def gcd_bl(A):

    left = [0 for _ in range(N + 1)]
    right = [0 for _ in range(N + 1)]
    ans = [0 for _ in range(N)]

    left[1] = A[0]
    for i in range(1, N):
        left[i + 1] = gcd_(left[i], A[i])
    right[-1 - 1] = A[-1]
    for i in range(1, N):
        right[-1 - i - 1] = gcd_(right[-1 - i], A[-1 - i])
    for i in range(N):
        ans[i] = gcd_(left[i], right[i + 1])
        
    return ans

def cin():
    in_ = list(map(int,input().split()))
    if len(in_) == 1:  return in_[0]
    else:  return in_

N = cin()
A = cin()
ans = 0
g = gcd_bl(A)
print(max(g))