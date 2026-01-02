def ri(): return int(input())
def rli(): return list(map(int, input().split()))
def rls(): return list(map(str, input().split()))
def pl(a): print(" ".join(list(map(str, a))))


N = ri()
a = rls()
bubble = a[:]

flag = True
while(flag):
    flag = False
    for i in range(1, N):
        if(bubble[-i][1] < bubble[-i-1][1]):
            hold = bubble[-i]
            bubble[-i] = bubble[-i-1]
            bubble[-i-1] = hold
            flag = True
pl(bubble)
print("Stable")  # ?????????Stable

selection = a[:]
for i in range(N):
    minj = i
    for j in range(i, N):
        if(selection[j][1] < selection[minj][1]):
            minj = j
    hold = selection[i]
    selection[i] = selection[minj]
    selection[minj] = hold

pl(selection)
print("Stable" if bubble == selection else "Not stable")