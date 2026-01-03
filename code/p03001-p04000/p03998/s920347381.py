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
    A = inputStrOnebyOne()
    B = inputStrOnebyOne()
    C = inputStrOnebyOne()

    check = "a"
    while True:
        if check == "a":
            if len(A) == 0:
                break
            check = A.pop(0)
        elif check == "b":
            if len(B) == 0:
                break
            check = B.pop(0)
        elif check == "c":
            if len(C) == 0:
                break
            check = C.pop(0)
    print(check.upper())
 
if __name__=='__main__':
    main()