#-*-coding:utf-8-*-

#遇奇判定
def isALLEven(arr):
    for i in arr:
        if i % 2 != 0:
            return False
    return True

#2で割る関数
def devide(i):
    return i / 2

def main():
    count = 0
    #N入力
    n = int(input())
    #整数入力
    lists = list(map(int, input().split()))

    #rリストの中身が偶数ならカウンタを1進めて，配列の中身を2で割る
    while isALLEven(lists):
        count += 1
        lists = list(map(devide, lists))
    
    print("{}".format(count))
    
if __name__ == '__main__':
    main()