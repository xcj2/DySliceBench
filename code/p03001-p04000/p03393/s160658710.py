def ctoi(c):
    return ord(c) - 97


def itoc(i):
    return chr(i + 97)


def ans(S):
    l = len(S)
    if l != 26:
        alpha = [False] * 26
        for i in range(l):
            alpha[ctoi(S[i])] = True
        for j in range(26):
            if not alpha[j]:
                ret = S + itoc(j)
                return ret
    else:
        alpha = [True] * 26
        for i in range(l):
            if i == l-1:
                ret = str(itoc(ctoi(S[0])+1))
                # alpha[ctoi(S[0])+1] = True
                # alpha[ctoi(S[0])] = False
                # k = 0
                # while len(ret) < l:
                #     if not alpha[k]:
                #         ret += itoc(k)
                #     k += 1
                return ret
            else:
                for j in range(ctoi(S[l-i-1])+1, 26):
                    if not alpha[j]:
                        ret = S[:l-i-1] + itoc(j)
                        # alpha[j] = True
                        # alpha[ctoi(S[l-i-1])] = False
                        # k = 0
                        # while len(ret) < l:
                        #     if not alpha[k]:
                        #         ret += itoc(k)
                        #     k += 1
                        return ret
                alpha[ctoi(S[l-i-1])] = False


S = input()
if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
else:
    print(ans(S))