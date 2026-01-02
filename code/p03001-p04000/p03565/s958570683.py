import sys
def input():
    return sys.stdin.readline()[:-1]

def match(s, t, lt, offset):
    for i in range(lt):
        if t[i] != s[offset+i] and s[offset+i] != '?':
            return False
    return True

def main():
    S = input()
    T = input()
    len_S = len(S)
    len_T = len(T)
    ans = list(S.replace('?','a'))
    for i in range(len_S-len_T+1):
        offset = len_S-len_T-i
        if match(S, T, len_T, offset):
            for j in range(len_T):
                ans[offset+j] = T[j]
            break
    else:
        print('UNRESTORABLE')
        exit()
    print(''.join(ans))

if __name__ == "__main__":
    main()
