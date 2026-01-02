import itertools

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():

    N, K = ZZ()
    S = input()
    gr = itertools.groupby(S)
    l = []
    c = 0
    for i, j in gr:
        l.append([int(i), len(list(j))])
        if i == '0': c += 1
    if c <= K:
        print(N)
        return
    output = 0
    left = right = 0
    sum = c = 0
    while left < len(l):

        while right < len(l) and c < K:
            if l[right][0] == 0: c += 1
            sum += l[right][1]
            right += 1
        if right < len(l) and l[right][0] == 1:
            sum += l[right][1]
            right += 1
        output = max(output, sum)
        if right == left:
            right += 1
            left += 1
        else:
            if l[left][0] == 0: c -= 1
            sum -= l[left][1]
            left += 1
            while left < len(l) and c >= K:
                if l[left][0] == 0: c -= 1
                sum -= l[left][1]
                left += 1
    print(output)

    return

if __name__ == '__main__':
    main()
