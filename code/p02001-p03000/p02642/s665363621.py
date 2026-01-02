from sys import stdin
readline = stdin.readline
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())

def make_divisors(n):
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n//i)
    result.sort()
    return result

def main():
    N = i_input()
    A = i_list()
    ans = 0
    max_a = max(A)
    p = [0] * (max_a + 1)
    for i in A:
        for j in range(i , max_a + 1, i):
            p[j] += 1
    for i in A:
        if p[i] < 2:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
