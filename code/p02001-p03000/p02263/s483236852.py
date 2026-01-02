# 文字列の取得
S = [1000]
t = [0] * 100000
S = input().split()
MAX=100000

def isEmpty() :
    return 0

def isFull():
    return top >= MAX - 1

def push(x):
    global top
    x = int(x)
    if isFull():
        print("Error")
        exit
    top += 1
#    print ("top=" , top)
    t[top] = x

def pop():
    global top
    if isEmpty():
        print("Error")
        exit
    top -= 1
    return t[int(top+1)]

## メイン処理
a = 0
b = 0
top = 0

# print('S=',S)

for item in S:
#    print ("item=", item)
    if (item == '+'):
        a = pop()
        b = pop()
#        print('push=', a + b)
        push( a + b )
    elif (item == '-'):
        b = pop()
        a = pop()
#        print('push=', a - b)
        push(a - b)
    elif (item == '*'):
        a = pop()
        b = pop()
#        print('push=', a * b)
        push(a * b)
    else:
 #       print('push=', item)
        push(item)

print(pop())
