def tashizan(a, b):
    c = a + b
    return c


def hikizan(a, b):
    c = a - b
    return c


def kakezan(a, b):
    c = a * b
    return c


def warizan(a, b):
    c = a // b
    return c


def hantei(op):
    if op == "+":
        ans = tashizan(a, b)
    elif op == '-':
        ans = hikizan(a, b)
    elif op == '*':
        ans = kakezan(a, b)
    elif op == '/':
        ans = warizan(a, b)
    return ans


while True:
    a, op, b = input().split()   # 3変数ともに文字列として読み込む
    a = int(a)                   # a を整数に変換
    b = int(b)                   # b を整数に変換
    
    if op == "?":
        break
    else:
        print(hantei(op))

