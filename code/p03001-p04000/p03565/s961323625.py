def main():
    S = input()
    T = input()

    # K個ずれたところ始めてマッチするかどうか
    def match(k):
        ans = True
        for i in range(len(T)):
            if S[k+i] != T[i] and S[k+i] != '?':
                ans = False
            # print(i, S[k+i], T[i], ans)
        return ans

    def construct(k):
        s = list(S)
        for i in range(len(T)):
            s[k+i] = T[i]
        return "".join(s)


    back = None
    for i in range(len(S) - len(T) + 1):
        if match(i):
            back = i

    if back is None:
        print('UNRESTORABLE')
    else:
        s = construct(back)
        s = s.replace('?', 'a')
        print(s)

if __name__ == "__main__":
    main()