import sys
input = sys.stdin.readline

def main():
    n, c, k = input_list()
    arrivals = []
    for _ in range(n):
        arrivals.append(int(input()))
    arrivals.sort()
    count = 0
    limit = 0
    ans = 0
    for i, a in enumerate(arrivals):
        if limit and limit < a:
            limit = 0
            count = 0
            ans += 1
        if not limit:
            limit = a + k
        if a <= limit:
            count += 1
        if count == c:
            ans += 1
            count = 0
            limit = 0
    if count > 0:
        ans += 1
    print(ans)

def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
