# Input Part
N,K = map(int,input().split())
A = [int(input()) for _ in range(N)]

Amax = 3*10**5

# N: 処理する区間の長さ
N0 = 2**(Amax-1).bit_length()
INF = 0
data = [INF]*(2*N0)
# a_k の値を x に更新
def update(k, x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = max(data[2*k+1], data[2*k+2])
# 区間[l, r)の最小値
def query(l, r):
    L = l + N0; R = r + N0
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = max(s, data[R-1])

        if L & 1:
            s = max(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

def main():
    for i in range(N):
        tmin = max(0,A[i]-K)
        tmax = min(Amax,A[i]+K)+1
        update(A[i],query(tmin,tmax)+1)
        #print(data)
    print(data[0])
main()
