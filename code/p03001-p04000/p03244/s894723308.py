from collections import Counter

def solve(n, v):
    # すべて同じ値
    if len(set(v)) == 1:
        return len(v) / 2

    odd = []
    even = []

    for i, k in enumerate(v):
        if i % 2 == 0:
            even.append(k)
        else:
            odd.append(k)

    odd_dic = Counter(odd).most_common()
    even_dic = Counter(even).most_common()

    ans = 0

    if odd_dic[0][0] == even_dic[0][0]:
        if odd_dic[0][1] > even_dic[0][1]:
            odd_v = odd_dic[0][0]
            even_v = even_dic[1][0]
        elif odd_dic[0][1] < even_dic[0][1]:
            odd_v = odd_dic[1][0]
            even_v = even_dic[0][0]
        else:
            if odd_dic[1][1] >= even_dic[1][1]:
                odd_v = odd_dic[1][0]
                even_v = even_dic[0][0]
            else:
                odd_v = odd_dic[0][0]
                even_v = even_dic[1][0]
    else:
        odd_v = odd_dic[0][0]
        even_v = even_dic[0][0]

    for i in range(len(even)):
        if even_v != even[i]:
           ans += 1

        if odd_v != odd[i]:
            ans += 1

    return ans

def test():
    assert solve(4, [3, 1, 3, 2]) == 1
    assert solve(6, [105, 119, 105, 119, 105, 119]) == 0
    assert solve(4, [1, 1, 1, 1]) == 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    ans = solve(n, v)
    print(int(ans))

if __name__ == '__main__':
    # test()
    main()