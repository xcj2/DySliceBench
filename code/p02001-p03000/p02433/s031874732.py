num = int(input())
root = [None, None, None]   #[前の値、次の値、カーソル部のデータ]
root[1] = [root, None, None]
cursor = root[1]

def insert(x):
    global cursor

    cursor[0][1]= cursor[0] = cursor = [cursor[0], cursor, x]

def move(d):
    global cursor
    if d > 0:
        for i in range(d):
            cursor = cursor[1]  #d回だけcursorをたどる
    else:
        for i in range(-d):
            cursor = cursor[0]

def erase():
    global cursor
    cursor[1][0] = cursor[0]
    cursor = cursor[1]
    cursor[0][1] = cursor

for j in range(num):
    queryi = list(map(int, input().split()))

    if queryi[0] == 0:
        insert(queryi[1])
    elif queryi[0] == 1:
        move(queryi[1])
    else:
        erase()

root = root[1]
while root[1]:
    print(root[2])
    root = root[1]

