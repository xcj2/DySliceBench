def merge(a, left, mid, right):
    l, r = [], []
    for i in range(left, mid):
        l.append(a[i])
    l.append(float('inf'))
    for i in range(mid, right):
        r.append(a[i])
    r.append(float('inf'))
    i, j = 0, 0
    for k in range(left, right):
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1


def merge_sort(a, left, right):
    res = 0
    if left + 1 < right:
        mid = (left + right) // 2
        res += merge_sort(a, left, mid)
        res += merge_sort(a, mid, right)
        merge(a, left, mid, right)
        res += right - left
    return res

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = merge_sort(a, 0, len(a))
    print(' '.join(map(str, a)))
    print(ans)

if __name__ == '__main__':
    main()
