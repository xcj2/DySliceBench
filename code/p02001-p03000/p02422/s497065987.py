sentence = input()
jobs = int(input())

def my_print(s, x, y):
    print(s[x:y+1])

def my_replace(s, x, y, t):
    s = list(s)
    s[x:y+1] = t
    return "".join(s)

def my_reverse(s, x, y):
    s = list(s)
    ss = s[x:y+1]
    ss.reverse()
    s[x:y+1] = ss
    return "".join(s)

for _ in range(jobs):
    task = input().split()
    task[1], task[2] = int(task[1]), int(task[2])
    if task[0] == "print":
        my_print(sentence, task[1], task[2])
    elif task[0] == "replace":
        sentence = my_replace(sentence, task[1], task[2], task[3])
    elif task[0] == "reverse":
        sentence = my_reverse(sentence, task[1], task[2])
