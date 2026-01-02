def bubble_sort(c, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if c[j][1] < c[j-1][1]:
                c[j], c[j-1] = c[j-1], c[j]
    return c

def selection_sort(c, n):
    for i in range(n-1):
        minj = i
        for j in range(i+1, n):
            if c[j][1] < c[minj][1]:
                minj = j
        if i != j:
            c[i], c[minj] = c[minj], c[i]
    return c


def main():
    N = int(input())
    cards1 = input().split()
    cards2 = cards1.copy()

    bubble_sorted = bubble_sort(cards1, N)
    print(*bubble_sorted)
    print("Stable")
    
    select_sorted = selection_sort(cards2, N)
    print(*select_sorted)
    if bubble_sorted == select_sorted:
        print("Stable")
    else:
        print("Not stable")


if __name__ == "__main__":
    main()

