def read():
    S = str(input().strip())
    K = int(input().strip())
    return S, K

def rle_encode(S):
    S1 = S + '@'
    rle = list()
    head = 0
    for i in range(0, len(S1)):
        if S1[i] != S1[head]:
            rle.append((S1[head], i-head))
            head = i
    return rle

def solve(S, K):
    count = 0
    rle = rle_encode(S)
    if len(rle) == 1:
        return rle[0][1] * K // 2
    else:
        for c, n in rle:
            count += n // 2
        count *= K
        if rle[-1][0] == rle[0][0]:
            if rle[-1][1] % 2 == 1 and rle[0][1] % 2 == 1:
                count += (K-1)
    return count

if __name__ == '__main__':
    inputs = read()
    print("%d" % solve(*inputs))
