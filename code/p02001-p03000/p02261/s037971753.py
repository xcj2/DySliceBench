import re
import copy
pattern = r'([0-9])'
repatter = re.compile(pattern)

n = int(input())
text = input()

*lists, = text.split(" ")
lists2 = copy.copy(lists)
lists3 = copy.copy(lists)


# バブルソート
def bubble_sort(a):
    flag = 1
    i = 0
    while flag:
        flag = 0
        for j in range(n-1, i, -1):
            x = repatter.findall(a[j])
            y = repatter.findall(a[j-1])
            if x < y:
                a[j], a[j-1] = a[j-1], a[j]
                flag = 1
        i += 1
    print(*a)
    print("Stable")


# 選択ソート
def select_sort(a):
    for i in range(n):
        min_j = i
        for j in range(i+1, n):
            x = repatter.findall(a[j])
            y = repatter.findall(a[min_j])
            if x < y:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]
    print(*a)


def isStable(before, after):
    flag = True
    for i in range(n):
        for j in range(i+1, n):
            for a in range(n):
                for b in range(a+1, n):
                    x = repatter.findall(before[i])
                    y = repatter.findall(before[j])
                    if x == y and before[i] == after[b] and before[j] == after[a]:
                        flag = False
    if flag is True:
        print("Stable")
    else:
        print("Not stable")


bubble_sort(lists)
select_sort(lists2)
isStable(lists3, lists2)
