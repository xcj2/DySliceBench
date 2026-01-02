import math
def main():
    arg = getInput(input())
    # arg = getInput(1024)
    ans = process(arg)
    print(ans)
    
def process(arg):
    yen500 = math.floor(arg / 500)
    amari = arg % 500
    yen5 = math.floor(amari / 5)
    ans = 1000 * yen500
    ans = ans + yen5 * 5

    return ans

def getInput(input):
    # 行数
    n = 1
    # 戻り値
    ret = None

    if n == 1:
        pass
        # ret = input
        # ret = list(input)
        ret = int(input)
        # ret = input.split()
        # ret = list(map(int, input.split()))
        # ret = input.split('T')
    else:
        for x in range(n):
            # 取得したい形式に変換
            ret = input[x]

    return ret

if __name__ == '__main__':
    main()
