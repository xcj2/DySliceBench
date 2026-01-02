N = int(input())
A = [int(s) for s in input().split()]

action = [0] * N
money = 1000
kabu = []


def state(a, b):
    return 'up' if a - b >= 0 else 'down'


def buy(i):
    global money
    kabu.append([A[i], (money // A[i])])
    money = money - ((money // A[i]) * A[i])
    kabu.append([A[i], (money // A[i])])


def sell(i):
    global kabu
    global money
    if not kabu:
        buy(0)
    for value, count in kabu:
        money += A[i] * count
    kabu = []


st0 = state(A[1], A[0])
if st0 == 'up':
    buy(0)

for i in range(1, N - 1):
    st1 = state(A[i + 1], A[i])
    if st0 != st1:
        # action
        if st1 == 'up':
            buy(i)
        else:
            sell(i)
    st0 = st1

if kabu:
    sell(N - 1)


print(money)
