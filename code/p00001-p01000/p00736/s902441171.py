import re
# and
def and_def(a, b):
    return str(min(int(a), int(b)))

# or
def or_def(a, b):
    return str(max(int(a), int(b)))

# not
def not_def(a):
    return str(2 - int(a))

def match(struct):
    if re.fullmatch(r'\-[0,1,2]', struct):
        return not_def(struct[-1])
    if re.fullmatch(r'[0,1,2]\+[0,1,2]', struct):
        return or_def(struct[0], struct[-1])
    if re.fullmatch(r'[0,1,2]\*[0,1,2]', struct):
        return and_def(struct[0], struct[-1])
    if re.fullmatch(r'[0,1,2]', struct):
        return struct
    if re.fullmatch(r'\([0,1,2]\)', struct):
        return struct[1]
    return struct

def parse(struct):
    tmpstruct = ''
    check, minas = False, False
    if len(struct) == 1:
        return struct

    for i in range(len(struct)):
        if not check:
            if struct[i] == '(':
                check = [')', '(']
                tmp = 1
                num = i
            elif struct[i] == '-':
                check = ['0', '1', '2', '(']
                minas = True
                num = i
            else:
                tmpstruct += struct[i]

        else:
            if struct[i] in check:
                if struct[i] == ')':
                    tmp -= 1
                    if not tmp:
                        if not minas:
                            tmpstruct += parse(struct[num+1: i])
                        else:
                            tmpstruct += not_def(parse(struct[num + 1: i + 1]))
                            minas = False
                        check = False
                elif struct[i] == '(' and check == ['0', '1', '2', '(']:
                    check = [')', '(']
                    tmp = 1
                elif struct[i] == '(':
                    tmp += 1
                else:
                    tmpstruct += not_def(parse(struct[num + 1: i + 1]))
                    check = False
                    minas = False
        tmpstruct = match(tmpstruct)
    return tmpstruct


def change_PQR(string, P, Q, R):
    ret = ''
    for i in string:
        if i == 'P':
            ret += str(P)
        elif i == 'Q':
            ret += str(Q)
        elif i == 'R':
            ret += str(R)
        else:
            ret += i
    return ret


while True:
    struct = input()
    if struct == '.':
        break

    ans = 0
    for i in (0, 1, 2):
        for j in (0, 1, 2):
            for k in (0, 1, 2):
                tmpstr = struct
                if parse(change_PQR(tmpstr, i, j, k)) == '2':
                    ans += 1
    print(ans)

