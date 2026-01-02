#!/usr/bin/env python3.4

# abc128_c

def main():
    # Input
    n, m = [int(s) for s in input().split()]
    reports = [[int(s) for s in input().split()] for _ in range(m)]
    ps = [int(s) for s in input().split()]
    # Get ans
    def get_switch_lists():
        for i in range(2**n):
            yield [(i//2**k)%2 for k in range(n)]
    def get_odd(switch_list, repo):
        return sum(switch_list[r-1] for r in repo[1:]) % 2
    ans = 0
    for switch_list in get_switch_lists():
        qs = [get_odd(switch_list, repo) for repo in reports]
        if all(p==q for p, q in zip(ps, qs)):
            ans += 1
    # Output
    print(ans)

if __name__ == '__main__':
    main()

