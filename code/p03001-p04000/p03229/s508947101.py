def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort(reverse=True)

    if n % 2 == 0:
        print(even_pattern(a))
    else:
        print(max(odd_pattern1(a), odd_pattern2(a)))

def odd_pattern1(a):
    m = len(a) // 2
    s = 0
    s += 2 * sum(a[:m])
    s -= sum(a[m:m+2])
    s -= 2 * sum(a[m+2:])
    return s

def odd_pattern2(a):
    m = len(a) // 2 - 1
    s = 0
    s += 2 * sum(a[:m])
    s += sum(a[m:m+2])
    s -= 2 * sum(a[m+2:])
    return s

def even_pattern(a):
    m = len(a) // 2 - 1
    s = 0
    s += 2 * sum(a[:m])
    s += a[m]
    s -= a[m+1]
    s -= 2 * sum(a[m+2:])
    return s

main()
