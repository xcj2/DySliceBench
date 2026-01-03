import copy
def deleteStr(S, text):
    if len(S) < len(text):
        return S
    for i, letter in enumerate(text):
        if letter == S[i]:
            continue
        else:
            return S
    return S[len(text):]

def checkStr(S, text):
    if len(S) < len(text):
        return False
    for i, letter in enumerate(text):
        if letter == S[i]:
            continue
        else:
            return False
    return True

def main():
    S = input()

    for i in range(len(S)):
        S_len = len(S)
        if checkStr(S, 'dreamer'):
            if checkStr(S, 'dreamerase'):
                S = deleteStr(S, 'dream')
            else:
                S = deleteStr(S, 'dreamer')
        else:
            S = deleteStr(S, 'dream')

        if checkStr(S, 'eraser'):
            S = deleteStr(S, 'eraser')
        else:
            S = deleteStr(S, 'erase')

        if S_len == len(S):
            if S_len == 0:
                print('YES')
            else:
                print('NO')
            break


if __name__ == '__main__':
    main()