#! python3
# stack.py - ポーランド記法で記述された計算式を解くプログラム

# 必要な変数を定義する
stack = [None] # 空の配列、0番目は埋まっている
# top = 0  # 配列の中の、一番うしろの値、初期状態では0
MAX = 201  # 配列が持つことができる最大値

# 配列が空かどうかを判定する（真偽値を返す）
def isEmpty(top):
    return top == 0

# 配列がいっぱいになっているかどうかを判定する（真偽値を返す）
def isFull(top):
    return top >= MAX - 1

# 配列の一番うしろに値を追加する
def push(x, stack):
    if isFull(len(stack)):
        raise Exception  # オーバーフロー
    stack.append(x)
    return stack

# 配列の一番うしろから値を削除する
def pop(stack):
    if isEmpty(len(stack)):
        raise Exception  # アンダーフロー
    stack = stack.pop()
    return stack

# 入力を扱う
original_input_list = input().split(' ')
input_list = []
for items in original_input_list:
    if items.isdecimal():
        input_list.append(int(items))
    else :
        input_list.append(items)

# print(input_list)        

for items in input_list:
    if type(items) == int:
        push(items, stack)
    elif items == "+":
        first_digit = pop(stack)
        second_digit = pop(stack)
        calculated_digit = second_digit + first_digit
        push(calculated_digit, stack)
    elif items == "-":
        first_digit = pop(stack)
        second_digit = pop(stack)
        calculated_digit = second_digit - first_digit
        push(calculated_digit, stack)
    elif items == "*":
        first_digit = pop(stack)
        second_digit = pop(stack)
        calculated_digit = second_digit * first_digit
        push(calculated_digit, stack)
    elif items == "/":
        first_digit = pop(stack)
        second_digit = pop(stack)
        calculated_digit = second_digit / first_digit
        push(calculated_digit, stack)

# print(stack)
# print(first_digit)
# print(second_digit)
print(stack[-1])


