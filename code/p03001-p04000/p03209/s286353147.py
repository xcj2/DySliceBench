

def a(N):
    if N == 0:
        return 1
    else:
        return a(N-1)*2 + 3


def p(N):
    if N == 0:
        return 1
    else:
        return p(N-1)*2 + 1


def judge(N, X, an, pn, tp):
    # print('---------')
    sn = an
    sl = int((an - 3) / 2)
    pl = int((pn - 1) / 2)
    # print('TIme' + str(N))
    # print('X'+str(X))
    # print('sl'+str(sl))
    # print('sn' + str(sn))
    # print('tp' + str(tp))
    if X == 1:
        # print('Step1')
        if N == 0:
            return tp + 1
        else:
            return tp + 0
    elif (X > 1) & (X < sl+1):
        # print('Step2')
        return judge(N-1, X-1, sl, pl, tp)
    elif (X == sl + 1) | (X == sl + 2):
        # print('Step3')
        if X == sl + 1:
            tp = pl + tp
            return tp
        else:
            tp = pl + 1 + tp
            return tp
    elif (X > sl + 2) & (X < sn):
        # print('Step4')
        tp = pl + 1 + tp
        return judge(N-1, X-sl-2, sl, pl, tp)
    elif X == sn:
        # print('Step5')
        return tp + pn


N, X = map(int, input().split())
an = a(N)
pn = p(N)
tp = 0
result = judge(N, X, an, pn, tp)
# print(an)
# print(pn)
print(result)