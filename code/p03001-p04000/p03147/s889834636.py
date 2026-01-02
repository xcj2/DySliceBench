def clean(hh):
    while hh:
        if hh[0]==0:
            del hh[0]
        else:
            break

def apply(hh):
    dh = min(hh)
    return (dh, [h-dh for h in hh])

def solve(hh):
    clean(hh)
    if not hh:
        return 0
    ans = 0
    try:
        idx = hh.index(0)
        ans = solve(hh[idx+1::])
    except ValueError:
        idx = len(hh)
    lhh = hh[:idx]
    dh, lhh = apply(lhh)
    dh += ans
    return dh + solve(lhh)



def main():
    N = int(input())
    hh = list(map(int, input().split()))
    print(solve(hh))



if __name__ == '__main__':
    main()