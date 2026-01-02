import collections

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    H, W = ZZ()
    D = collections.defaultdict(int)
    for i in range(H):
        for c in input(): D[c] += 1

    if 1 in {H, W}:
        if H*W%2 == 0: print('Yes' if all([D[c]%2 == 0 for c in D.keys()]) else 'No')
        else:
            a = 0
            for c in D.keys():
                if D[c]%2 == 1: a += 1
            print('Yes' if a == 1 else 'No')
    else:
        if H%2 == 0 and W%2 == 0: print('Yes' if all([D[c]%4 == 0 for c in D.keys()]) else 'No')
        elif (H*W)%2 == 0:
            if W%2 == 0: H, W = W, H
            x = y = z = 0
            for c in D.keys():
                if D[c]%4 == 0: x += 1
                elif D[c]%4 == 2: y += 1
                else: z += 1
            print('Yes' if y%2 == (H//2)%2 and y <= H//2 and z == 0 else 'No')
        else:
            a = b = 0
            for c in D.keys():
                if D[c]%2 == 1: a += 1
                b += D[c]//4
            print('Yes' if a == 1 and b >= (H//2)*(W//2) and len(D.keys()) <= ((H+1)//2)*((W+1)//2) else 'No')
    return

if __name__ == '__main__':
    main()
