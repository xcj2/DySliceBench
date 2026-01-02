CARDMAX = 100
POINTMAX = 100
    
def main():
    head = []
    c_taro = []
    c_hana = []

    while True:
        # 初期化
        head.clear()
        c_taro.clear()
        c_hana.clear()

        # 先頭情報
        head = input()
        head = head.split(" ")

        # 終了処理
        if head == ['0', '0']:
            return 0

        for j in range(int(head[0])):
            c_taro.append(int(input()))

        for j in range(int(head[1])):
            c_hana.append(int(input()))

        sum_taro = showsum(c_taro)
        sum_hana = showsum(c_hana)
        avee = showave(sum_taro, sum_hana)
        toave = avee - sum_taro

        print(showchcard(c_taro, c_hana, toave))
"""
        print("headdata::")
        print(head)
        print("c_taro::")
        print(c_taro)
        print("c_hana::")
        print(c_hana)
        print("sum_taro::")
        print(sum_taro)
        print("sum_hana::")
        print(sum_hana)
        print("average::")
        print(avee)
        print("")
"""

def showsum(array):
    summ = 0
    for item in array:
        summ += item
    return summ

def showave(a, b):
    return (a + b) / 2

def showchcard(tarray, harray, toave):
    wa = CARDMAX * 2 + 1
    for tnum in tarray:
        for hnum in harray:
            if hnum - tnum == toave:
                if wa >= (hnum + tnum):
                    tans = tnum
                    hans = hnum
                    wa = tans + hans

    if wa != CARDMAX * 2 + 1:
        result = str(tans) + " " + str(hans)
        return result
    else:
        return -1

main()

