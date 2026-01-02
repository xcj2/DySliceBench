n, a, b, c = map(int, input().split())

abc = [a, b, c]

def yes():
    print('Yes')
    for c in ans:
        print(chr(c+ord('A')))

def no():
    print('No')
    exit()

def move(s, t):
    ans.append(s)
    abc[s] += 1
    abc[t] -= 1

play = []

for i in range(n):
    s = bytes(input(), 'ascii')
    s, t = s[0]-ord('A'), s[1]-ord('A')

    play.append((s, t))

ans = []
for i, (s, t) in enumerate(play):
    if abc[s] == 0 and abc[t] == 0:
        no()
        break
    if abc[s] == abc[t]:
        if s in play[(i+1)%n]:
            move(s, t)
        else:
            move(t, s)
    elif abc[s] < abc[t]:
        move(s, t)
    else:
        move(t, s)

yes()