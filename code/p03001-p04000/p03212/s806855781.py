def change_ten_to_kisu(num, kisu):      # 10進数をkisu進数に変換 (int, int) => int
    r = 0
    syo = num
    count = 0
    while syo >= kisu:
        r += (syo % kisu) * 10 ** count
        syo = syo // kisu
        count += 1
    return r + syo * 10 ** count

def change_kisu_to_ten(num, kisu):      # kisu進数を10進数に変換 (int, int) => int
    n = str(num)
    r = 0
    for i in range(len(n)):
        r += int(n[-i - 1]) * kisu ** i
        # print(r, int(n[-i - 1]), kisu ** i)
    return r

def plus(num):                   # 3, 5, 7のみを使用しnumより大きい数を返す
    change = {"3" : "0", "5" : "1", "7" : "2"}
    change_r = {"0" : "3", "1" : "5", "2" : "7"}
    t = ""
    for i in str(num):
        t += change[i]
    r = change_ten_to_kisu(change_kisu_to_ten(int(t), 3) + 1, 3)
    if len(t) < len(str(r)):
        r = "0" + str(r)[1:]
    elif len(t) > len(str(r)):
        r = "0" * (len(t) - len(str(r))) + str(r)
    t = ""
    for i in str(r):
        t += change_r[i]
    return int(t)

N = int(input())

i = 3
count = 0
while i <= N:
    if "3" in str(i) and "5" in str(i) and "7" in str(i):
        # print(i)
        count += 1
    i = plus(i)
print(count)