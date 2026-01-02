def pad(S,N):
    return (N-len(S)) * "0" + S

def xor_sum(A,M):
    N = len(A)
    bit_count = [0 for _ in range(60)]
    #bit_count[i]:iビット目が1であるa in Aの個数

    for i in range(N):
        A[i] = pad(bin(A[i])[2:],60)
        for j in range(60):
            if A[i][60-j-1] == "1":
                bit_count[j] += 1

    output = 0
    for j in range(60):
        tmp1 = (N-bit_count[j])*bit_count[j] % M
        tmp2 = pow(2,j,M)
        tmp = (tmp1 * tmp2) % M
        output += tmp
        output %= M

    return output

def main():
    N = int(input())
    A = list(map(int,input().split()))
    M = 10**9+7

    print(xor_sum(A,M))

if __name__ == "__main__":
    main()
