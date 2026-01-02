"""
                            pppppppppppppppppppp
                         ppppp  ppppppppppppppppppp
                      ppppppp    ppppppppppppppppppppp
                      pppppppp  pppppppppppppppppppppp
                      pppppppppppppppppppppppppppppppp
                              pppppppppppppppppppppppp
       ppppppppppppppppppppppppppppppppppppppppppppppp  pppppppppppppppppppp
      pppppppppppppppppppppppppppppppppppppppppppppppp  ppppppppppppppppppppp
     ppppppppppppppppppppppppppppppppppppppppppppppppp  pppppppppppppppppppppp
    ppppppppppppppppppppppppppppppppppppppppppppppp    pppppppppppppppppppppppp
   pppppppppppppppppppppppppppppppppppppppppppppp     pppppppppppppppppppppppppp
  ppppppppppppppppppppppppppppppppppppppppppppp      pppppppppppppppppppppppppppp
  pppppppppppppppppppppppppppppppp               pppppppppppppppppppppppppppppppp
  pppppppppppppppppppppppppppp     pppppppppppppppppppppppppppppppppppppppppppppp
  ppppppppppppppppppppppppppp    pppppppppppppppppppppppppppppppppppppppppppppppp
    pppppppppppppppppppppppp  pppppppppppppppppppppppppppppppppppppppppppppppppp
     ppppppppppppppppppppppp  ppppppppppppppppppppppppppppppppppppppppppppppppp
      pppppppppppppppppppppp  ppppppppppppppppppppppppppppppppppppppppppppppp
       ppppppppppppppppppppp  ppppppppppppppppppppppppppppppppppppppppppppp
                              pppppppppppppppppppppppp
                              pppppppppppppppppppppppppppppppp
                              pppppppppppppppppppppp  pppppppp
                              ppppppppppppppppppppp    ppppppp
                                 ppppppppppppppppppp  ppppp
                                    pppppppppppppppppppp
"""


import sys
def data(): return sys.stdin.readline().strip()
def out(var): sys.stdout.write(str(var))
def outa(*var, end="\n"): sys.stdout.write(' '.join(map(str, var)) + end)
def l(): return list(sp())
def sp(): return map(int, data().split())


def calculate(string):
    result = 0
    while string:
        c = bin(string)[2:].count('1')
        string = string % c
        result += 1
    return result


n = int(data())
s = list(data())
ones = []
powers = []
for i in range(n):
    if s[i] == '1':
        ones.append(i)
length = len(ones)
powers = [[0, 0] for i in range(n)]
for i in range(n):
    if length - 1 > 0:
        powers[i][0] = pow(2, i, length-1)
    powers[i][1] = pow(2, i, length + 1)
powers = powers[::-1]
s1, s2 = 0, 0
for i in ones:
    if length - 1 > 0:
        s1 = (s1 + powers[i][0])
    s2 = (s2 + powers[i][1])
for i in range(n):
    if s[i] == '1':
        if length - 1 <= 0:
            out("0\n")
            continue
        temp = s1
        temp = (temp - powers[i][0] + length - 1) % (length - 1)
    else:
        temp = s2
        temp = (temp + powers[i][1]) % (length + 1)
    out(str(calculate(temp)+1)+"\n")
