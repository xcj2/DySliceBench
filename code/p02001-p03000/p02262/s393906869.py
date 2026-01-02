# シェルソート
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_D&lang=jp
# 挿入ソートを応用してn個の整数を含む数列Aを昇順に整列するプログラム

def show(array):
    for i in range(len(array)):
        if (i+1) >= len(array):
            print(array[i])
        else:
            print(array[i], end=' ')

def insertion_sort(c, g):
    n = len(c)
    count = 0
    for i in range(g, n):
        v = c[i]
        j = i - g
        while j >= 0 and c[j] > v:
            c[j+g] = c[j]
            j = j - g
            count += 1
        c[j+g] = v
    return c, count


def shell_sort(c, G):
    counts = 0
    for g in G:
        co, count = insertion_sort(c, g)
        counts += count
    return co, counts


def main():
    n = int(input())
    c = [int(input()) for _ in range(n)]

    # For making G
    n = len(c)
    g = []
    for m in range(1, 100):
        t = (3 ** m - 1) // 2
        if t > n:
            break
        g.append(t)
    g = g[::-1]

    result, count = shell_sort(c, g)

    print(m-1)
    show(g)
    print(count)
    for num in result:
        print(num)

main()
