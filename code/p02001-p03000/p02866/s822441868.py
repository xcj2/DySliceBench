import collections
import sys
def read_a_integer():
    return int(sys.stdin.readline())

def read_a_list(dtype):
    return list(map(dtype, sys.stdin.readline().split()))


def main():
    N = read_a_integer()
    D = read_a_list(int)
    if D[0] != 0:
        print(0)
        return
    counter = collections.Counter(D)
    if counter[0] != 1:
        print(0)
        return
    max_D = max(D)
    ans = 1
    for i in range(2, max_D + 1):
        if i not in counter:
            print(0)
            return
        ans = (ans * (counter[i-1] ** counter[i])) % 998244353
    print(ans)
    # brute_force(N, D)

        


if __name__ == "__main__":
    main()
