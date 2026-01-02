"""
J氏は、メッセージのすべての文字を左に1つ回転させます。
たとえば、「aB23d」を「B23da」に変換します。

ミスCは、メッセージのすべての文字を1つ右に回転します。
たとえば、彼女は「aB23d」を「daB23」に変換します。

E氏はメッセージの左半分を右半分と入れ替えます。メッセージの文字数が奇数の場合、中央の文字は移動しません。
たとえば、「e3ac」を「ace3」に、「aB23d」を「3d2aB」に変換します。

A氏はメッセージを逆にします。たとえば、「aB23d」を「d32Ba」に変換します。

Dr. Pは、メッセージ内のすべての数字を1つ増やします。数字が「9」の場合、「0」になります。アルファベットは変更されません。
たとえば、彼は「aB23d」を「aB34d」に、「e9ac」を「e0ac」に変換します。

M氏は、メッセージのすべての桁を1つ減らします。数字が「0」の場合、「9」になります。アルファベットは変更されません。
たとえば、彼は「aB23d」を「aB12d」に、「e0ac」を「e9ac」に変換します。
"""

def func_by_J(t):
    return t[len(t)-1] + t[:len(t)-1]

def func_by_C(t):
    return t[1:len(t)] + t[0]

def func_by_E(t):
    if len(t)%2 == 0:
        t = t[len(t)//2:] + t[:len(t)//2]
    else:
        t = t[len(t)//2+1:] + t[len(t)//2] + t[:len(t)//2]
    return t

def func_by_A(t):
    return t[::-1]

def func_by_P(t):
    s = []
    for c in t:
        try:
            integer = int(c)
            s.append(str((integer - 1)%10))
        except:
            s.append(c)

    return "".join(s)

def func_by_M(t):
    s = []
    for c in t:
        try:
            integer = int(c)
            s.append(str((integer + 1)%10))
        except:
            s.append(c)

    return "".join(s)


def solve(s, t):
    for c in reversed(s):
        if c == "J":
            t = func_by_J(t)
        elif c == "C":
            t = func_by_C(t)
        elif c == "E":
            t = func_by_E(t)
        elif c == "A":
            t = func_by_A(t)
        elif c == "P":
            t = func_by_P(t)
        elif c == "M":
            t = func_by_M(t)
    return t


if __name__ == '__main__':
    #"""
    n = int(input())
    ans = []
    for i in range(n):
        s = input()
        t = input()
        ans.append(solve(s, t))
    print(*ans, sep="\n")

    """
    t = "abcd019"
    print(t)
    print(func_by_J(t))
    print(func_by_C(t))
    print(func_by_E(t))
    print(func_by_A(t))
    print(func_by_P(t))
    print(func_by_M(t))
    """

