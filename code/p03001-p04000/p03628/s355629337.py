
MOD = 10 ** 9 + 7

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    S = [input() for _ in range(2)]
    d = []
    i = 0
    while i < N:
        if S[0][i] == S[1][i]:
            i += 1
            d.append(0)
        else:
            i += 2
            d.append(1)
    output = 6 if d[0] else 3
    for i in range(len(d)-1):
        if d[i+1] == 0 and d[i] == 0: output *= 2
        elif d[i+1] == 0 and d[i] == 1: continue
        elif d[i+1] == 1 and d[i] == 0: output *= 2
        else: output *= 3
        output %= MOD
    print(output)

    return

if __name__ == '__main__':
    main()
