import collections

#文字列を一文字ずつ取得したいとき
def inputStrOnebyOne():
    s = list(input())
    return s

#整数を一つずつリストに入れる
def inputOnebyOne_Int():
    a = list(int(x) for x in input().split())
    return a

def main():
    s = inputStrOnebyOne()
    ret = []
    for i in range(len(s)):
        if s[i] == "0":
            ret.append(s[i])
        elif s[i] == "1":
            ret.append(s[i])
        else:
            if 1<=len(ret):
                ret.pop()
    print(''.join(ret))

if __name__=='__main__':
    main()