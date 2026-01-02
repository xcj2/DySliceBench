N = int(input())
S = list(input())
Q = int(input())
query = [input().split() for _ in range(Q)]

bit = [[0 for _ in range(26)] for _ in range(N + 1)]



def bit_add(i, s):
    ss = ord(s) - ord("a")
    while i <= N:
        bit[i][ss] += 1
        i += i & - i
def bit_add2(i, s):
    ss = ord(s) - ord("a")
    while i <= N:
        bit[i][ss] += -1
        i += i & - i
        
def bit_sum(i):
    s = [0] * 26
    while i:
        for j in range(26):
            s[j] += bit[i][j]
        i -= i & -i
    return s
for i in range(1, N + 1):
    s = S[i - 1]
    bit_add(i, s)



for x, y, z in query:
    if x == "1":
        y = int(y)
        bit_add2(y, S[y - 1])
        bit_add(y, z)
        S[y - 1] = z
    if x == "2":
        answer = 0
        y, z = int(y) - 1, int(z)
        yy = bit_sum(y)
        zz = bit_sum(z)
        #print(yy)
        #print(zz)
        for i in range(26):
            if zz[i] - yy[i] > 0:
                answer += 1
        print(answer)
    #print(S)
    #print(bit_sum(N))