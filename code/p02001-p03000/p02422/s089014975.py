def main():

    strTxt = input()
    n = int(input())
    for _ in range(n):
        strCmd = input().split()
        
        if strCmd[0] == 'print':
            funcPrint(strTxt, int(strCmd[1]), int(strCmd[2]))
        elif strCmd[0] == 'reverse':
            strTxt = funcReverse(strTxt, int(strCmd[1]), int(strCmd[2]))
        elif strCmd[0] == 'replace':
            strTxt = funcReplace(strTxt, int(strCmd[1]), int(strCmd[2]), strCmd[3])

def funcPrint(strInput: str,a: int,b: int):
    print(strInput[a:b+1])

def funcReverse(strInput: str,a: int,b: int):
    return strInput[:a]+strInput[a:b+1][::-1]+strInput[b+1:]

def funcReplace(strInput: str,a: int,b: int, strAfter: str):
    return strInput[:a]+strAfter+strInput[b+1:]


if __name__ == '__main__':
    main()

