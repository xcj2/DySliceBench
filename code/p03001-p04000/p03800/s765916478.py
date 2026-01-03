a = int(input())
s = input()
l = len(s)
target = [None for x in s]
target[0] = True
target[1] = True


def fill(b, n, i):
    if s[i] == "o":
        target[b] = target[n] if target[i] else not target[n]
    else:
        target[b] = not target[n] if target[i] else target[n]


def jud(b, n, i):
    if s[i] == "o":
        return target[b] == (target[n] if target[i] else not target[n])
    else:
        return target[b] == (not target[n] if target[i] else target[n])
    

def result(s1, s2):
    global target
    target = [None for x in s]
    target[0] = s1
    target[1] = s2
    for i in range(1, len(s)):
        b, n = i - 1, (i + 1) % l
        fill(n, b, i)
    return jud(-1, 1, 0) and jud(0, 2, 1)

for p in [[True, True], [True, False], [False, True], [False, False]]:
    if result(*p):
        print("".join(["S" if x else "W" for x in target]))
        break
else:
    print(-1)