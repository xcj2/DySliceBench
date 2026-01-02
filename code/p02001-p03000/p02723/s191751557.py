def main():
    arg = getInput(input())
    # arg = getInput(input())
    ans = process(arg)
    print(ans)
    
def process(arg):
    cof = list('coffee')
    if arg[2] == arg[3] and arg[4] == arg[5]:
        ans = "Yes"
    else:
        ans = "No"

    return ans

def getInput(input):
    # 行数
    n = 1
    # 戻り値
    ret = None

    if n == 1:
        pass
        # ret = input
        ret = list(input)
        # ret = int(input)
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