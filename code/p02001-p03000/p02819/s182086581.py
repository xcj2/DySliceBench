import math

# 素数判定関数
def isPrime(num):
    # 2未満の数字は素数ではない
    if num < 2: return False
    # 2は素数
    elif num == 2: return True
    # 偶数は素数ではない
    elif num % 2 == 0: return False

    # 3 ~ numまでループし、途中で割り切れる数があるか検索
    # 途中で割り切れる場合は素数ではない
    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False

    # 素数
    return True

# 素数判定
def callIsPrime(input_num):
    # ループしながら素数を検索する
    for i in range(input_num, input_num+1000):
        if isPrime(i):
            primenumber = i
            break

    # 素数配列を返す
    return primenumber

def main():
    X = int(input())

    ans = callIsPrime(X)

    print(ans)
 
if __name__ == '__main__':
    main()