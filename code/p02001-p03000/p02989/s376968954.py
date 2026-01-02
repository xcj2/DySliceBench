import bisect
import sys

verbose = False

def test(d, k):
    sd = sorted(d)
    uniq_d = []
    pop_d = {}
    for num in sd:
        if num in pop_d:
            pop_d[num] += 1
        else:
            pop_d[num] = 1
            uniq_d.append(num)
    uniq_d = sorted(uniq_d)
    pop_uniq_d = []
    cum_pop_uniq_d = []
    prev_pop = 0
    for num in uniq_d:
        pop = pop_d[num]
        pop_uniq_d.append(pop)
        prev_pop += pop
        cum_pop_uniq_d.append(prev_pop)
    if prev_pop % 2 == 1:
        return 0
    if verbose:
        print("total pop =", prev_pop)
    target = prev_pop // 2
    if verbose:
        print("target = ", target)
    target_off = bisect.bisect_right(cum_pop_uniq_d, target)
    if verbose:
        print("target_off = ", target_off)
    if target_off == 0:
        return 0
    if verbose:
        print( "uniq_d = ", uniq_d)
        print( "cum_pop = ", cum_pop_uniq_d)
        print( "uniq_d[target_off] = ", uniq_d[target_off])
        print( "cum_pop_uniq_d[target_off] = ", cum_pop_uniq_d[target_off])
    if cum_pop_uniq_d[target_off-1] != target:
        return 0
    ans = uniq_d[target_off] - uniq_d[target_off-1]
    return ans


def main():
    rv = 0
    #with sys.stdin as input:
    input = sys.stdin
    Nline = input.readline()
    N = int(Nline)
    args = input.readline()
    vargs = args.split()
    d = [int(arg) for arg in vargs]
    rv = test(d, N)
    print(rv)

def mock():
    rv = test( [9, 1, 4, 4, 6, 7], 6)
    print(rv)
    rv = test([9, 1, 14, 5, 5, 4, 4, 14], 8)
    print(rv)
    rv = test([99592, 10342, 29105, 78532, 83018, 11639, 92015, 77204, 30914, 21912, 34519, 80835, 100000, 1], 14)
    print(rv)

if __name__ == '__main__':
    main()