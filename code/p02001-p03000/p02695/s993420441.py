import itertools

def main():
    m = 100
    n, m, q = input_list()
    queries = []
    for _ in range(q):
        queries.append(input_list())
    a = []
    for i in range(1, m+1):
        a.append(i)
    ans = []
    for i in itertools.combinations_with_replacement(a, n):
        ans.append(calc(i, queries))
    print(max(ans))


def calc(i, queries):
    ans = 0
    for q in queries:
        a, b, c, d = q
        if i[b-1] - i[a-1] == c:
            ans += d
    #print(i, ans)
    return ans

def input_list():
    return list(map(int, input().split()))


if __name__ == '__main__':
    main()
