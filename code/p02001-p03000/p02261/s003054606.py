def bubble_sort(c, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if int(c[j][1]) < int(c[j-1][1]):
                c[j], c[j-1] = c[j-1], c[j]
    return c

def selection_sort(c, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(c[j][1]) < int(c[minj][1]):
                minj = j
        c[i], c[minj] = c[minj], c[i]
    return c

def is_stable(original_list, sorted_list):
    for target in sorted_list:
        for original in original_list:
            if target[1] == original[1]:
                if target[0] != original[0]:
                    return "Not stable"
                original_list.remove(original)
                break
    return "Stable"
                
if __name__ == "__main__":
    import copy
    n = int(input())
    c = input().split()
    bubble_list = bubble_sort(copy.deepcopy(c), n)
    print(*bubble_list)
    print(is_stable(copy.deepcopy(c), bubble_list))
    selection_list = selection_sort(copy.deepcopy(c), n)
    print(*selection_list)
    print(is_stable(copy.deepcopy(c), selection_list))
