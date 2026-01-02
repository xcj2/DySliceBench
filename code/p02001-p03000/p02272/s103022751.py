def merge(a, left, mid, right):
    INF = int(1e+11)
    l = a[left:mid]
    r = a[mid:right]
    l.append(INF)
    r.append(INF)
    i = 0
    j = 0

    ans = 0

    for k in range(left, right):
        ans += 1
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
    
    return ans


def merge_sort(a, left, right):
    ans = 0
    if left + 1 < right:
        mid = (left + right) // 2
        ans += merge_sort(a, left, mid)
        ans += merge_sort(a, mid, right)
        ans += merge(a, left, mid, right)
    return ans


def print_list_split_whitespace(s):
    for x in s[:-1]:
        print(x, end=" ")
    print(s[-1])

n = int(input())
s = [int(x) for x in input().split()]

ans = merge_sort(s, 0, len(s))

print_list_split_whitespace(s)
print(ans)
