def BubbleSort(n, lst):
    for i in range(n):
        for j in range(n-1, i, -1):
            if lst[j][1] < lst[j-1][1]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst

def SelectionSort(n, lst):
    for i in range(n):
        minj = i
        for j in range(i+1, n):
            if lst[j][1] < lst[minj][1]:
                minj = j
        if minj != i:
            lst[i], lst[minj] = lst[minj], lst[i]
    return lst

#バブルソートは必ず安定なので１つめのソート結果と比較することで
#O(N)で２つ目のソートの安定性を判定できる
def check(lst1, lst2):
    if lst1 == lst2:
        print("Stable")
    else:
        print("Not stable")

"""
def check(n, lst_o, lst):
    keeper = [[]]*10
    keeper2 = [[]]*10
    for i in range(n):
        keeper[int(lst_o[i][1])] = keeper[int(lst_o[i][1])] + [lst_o[i][0]]
        keeper2[int(lst[i][1])] = keeper2[int(lst[i][1])] + [lst[i][0]]
    if keeper == keeper2:
        print("Stable")
    else:
        print("Not stable")
"""

n = int(input())
lst = input().split()
lst1 = BubbleSort(n, lst.copy())
print(*lst1)
#check(n, lst.copy(), lst1)
print("Stable")
lst2 = SelectionSort(n, lst.copy())
print(*lst2)
check(lst1, lst2)
#check(n, lst.copy(), lst2)


