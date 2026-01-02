N = int(input())
l = list(map(int, input().split()))

# リストを受け取り、すべてが偶数かどうかチェックする
def is_even(a):
    for i in a:
        if i % 2 != 0:
            return False
    return True

# リストを受け取り、すべてを÷2したリストを返却する
def divided_list(a):
    tmp_list = []
    for k in a:
        tmp_list.append(int(k / 2))
    return tmp_list

# リストを受け取り、すべてが偶数であればすべてを÷2したリストを返却し、それ以外の場合はFalseを返却する
def aaa(a):
    if is_even(l):
        return divided_list(l)
    else:
        return False

count = 0
while aaa(l):
    count += 1
    l = aaa(l)

print(count)