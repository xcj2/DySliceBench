class Card:
    def __init__(self, s, i):
        self.suit = s[0]
        self.value = s[1]
        self.iniorder = i

def BubbleSort(C, N):
    for i in range(N):
        for j in range(N - 1, i, -1):
            if C[j].value < C[j - 1].value:
                C[j], C[j - 1] = C[j - 1], C[j]

    return C

def SelectionSort(C, N):
    for i in range(N):
        minj = i

        for j in range(i, N):
            if C[j].value < C[minj].value:
                minj = j

        C[i], C[minj] = C[minj], C[i]

    return C


n = int(input())
cards = [Card(c, i) for (i, c) in enumerate(input().split())]

res_bub = BubbleSort(cards[:], n)
res_sel = SelectionSort(cards[:], n)

print(*[c.suit + c.value for c in res_bub])

for i in range(n - 1):
    if res_bub[i].value == res_bub[i + 1].value:
        if res_bub[i].iniorder > res_bub[i + 1].iniorder:
            print("Not stable")
            break
else:
    print("Stable")

print(*[c.suit + c.value for c in res_sel])

for i in range(n - 1):
    if res_sel[i].value == res_sel[i + 1].value:
        if res_sel[i].iniorder > res_sel[i + 1].iniorder:
            print("Not stable")
            break
else:
    print("Stable")