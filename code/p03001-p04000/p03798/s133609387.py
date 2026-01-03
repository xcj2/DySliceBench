n = int(input())
s = input()

def make_list(li):
    for i in range(2, n):
        if li[i-1] == 'S':
            if s[i-1] == 'o':
                li[i] = li[i-2]
            else:
                if li[i-2] == 'S':
                    li[i] = 'W'
                else:
                    li[i] = 'S'
        else:
            if s[i-1] == 'o':
                if li[i-2] == 'S':
                    li[i] = 'W'
                else:
                    li[i] = 'S'
            else:
                li[i] = li[i-2]

    hantei(li)

def hantei(li):
    flag = True
    for i in range(2):
        if li[-i] == 'S':
            if s[-i] == 'o':
                if li[-1-i] != li[1-i]:
                    flag = False
            else:
                if li[-1-i] == li[1-i]:
                    flag = False
        else:
            if s[-i] == 'o':
                if li[-1-i] == li[1-i]:
                    flag = False
            else:
                if li[-1-i] != li[1-i]:
                    flag = False

    if flag:
        print_list(li)

def print_list(li):
    for i in li:
        print(i, end = '')
    exit()

li = [[''] * n for _ in range(4)]
li[0][0] = 'S'
li[0][1] = 'S'
li[1][0] = 'S'
li[1][1] = 'W'
li[2][0] = 'W'
li[2][1] = 'S'
li[3][0] = 'W'
li[3][1] = 'W'

for i in range(4):
    make_list(li[i])

print(-1)
