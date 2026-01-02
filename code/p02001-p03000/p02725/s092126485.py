def main():
    input1 = input()
    input2 = input()
    k , n = map(int , input1.split())
    al = list(map(int , input2.split()))
    arg = [[k,n],al]
    ans = process(arg)
    print(ans)
    
def process(arg):
    ans = 0
    ensyu = arg[0][0]
    kensu = arg[0][1]
    aida = list()
    for x in range(arg[0][1]):
        mae = arg[1][x-1]
        b = arg[1][x]
        if x == 0:
            # 1件目は演習
            w = b + ensyu - arg[1][kensu-1]
        else:
            w = b - mae
        aida.append(w)

    m = max(aida)
    flg = False
    for y in aida:
        if flg == True or y != m :
            ans = ans + y
        else:
            flg = True
    return ans

def getInput(input):

    return 

if __name__ == '__main__':
    main()
