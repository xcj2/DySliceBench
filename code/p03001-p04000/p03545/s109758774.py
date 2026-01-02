import sys
tmp = input()
a = int(tmp[0])
b = int(tmp[1])
c = int(tmp[2])
d = int(tmp[3])
def tonum(a, n):
    if (a == 0):
        return n
    else:
        return - 1 * n
def operand(n):
    if (n == 0):
        return '+'
    else:
        return '-'

def format(a, b, c, d, ab, bc, cd):
    string = str(a) + operand(ab) + str(b) + operand(bc) + str(c) + operand(cd) + str(d)+'=7'
    return string
tmp=0
for i in range(2):
    for j in range(2):
        for k in range(2):
                tmp = a+tonum(i, b)+tonum(j, c)+tonum(k,d)
                if (tmp == 7):
                    print(format(a, b, c, d, i, j, k))
                    sys.exit()
