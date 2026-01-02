m = 1046527
H = [""] * m


def str_to_nume(word):
    ans = ""
    for _ in word:
        if _ == "A":
            ans += ("1")
        elif _ == "C":
            ans += ("2")
        elif _ == "G":
            ans += ("3")
        elif _ == "T":
            ans += ("4")
    return ans


def convert_type(word):
    # print("word", word)
    # print("value", int(str_to_nume(word)))
    return int(str_to_nume(word))


def hash1(key):
    return key % m


def hash2(key):
    '''hash1で衝突したとき用
    '''
    return 1 + key % (m-1)


def find(str_key):
    key = convert_type(str_key)
    for i in range(m):
        h = (hash1(key) + i * hash2(key)) % m
        if H[h] == str_key:
            return 1
        elif len(H[h]) == 0:
            return 0
    return 0


def insert(str_key):
    key = convert_type(str_key)
    for i in range(m):
        h = (hash1(key) + i * hash2(key)) % m
        if H[h] == str_key:
            return 1
        elif len(H[h]) == 0:
            H[h] = str_key
            return 0
    return 0


sols = []
n = int(input())
# print("hoge")
for i in range(n):
    col = input().split()
    if col[0] == "insert":
        insert(col[1])
    else:
        if find(col[1]) == 1:
            sols.append("yes")
        else:
            sols.append("no")
for _ in sols:
    print(_)

