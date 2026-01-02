N=int(input())
target_h=map(int,input().split(' '))


def all_zero(h):
    zero = True
    for hh in h:
        if hh != 0:
            zero = False
            break
    return zero

def div_ary(h):
    arys = []
    zeropos = []

    for i,hh in enumerate(h):
        if hh == 0:
            zeropos.append(i)
    
    if len(zeropos) == 0:
        return [h]
    else:
        tmpary = []
        for i, hh in enumerate(h):
            if hh == 0:
                arys.append(tmpary)
                tmpary = []
            else:
                tmpary.append(hh)
        arys.append(tmpary)
    return arys

#minが0になるまで全体に水やり
def mizuyari(h_ary):
    if len(h_ary) == 0:
        return 0
    else:
        #minまでは水やり
        h_min = min(h_ary)
        for i in range(len(h_ary)):
            h_ary[i] -= h_min
        num = h_min

        #すべてゼロなら回数決定
        if all_zero(h_ary):
            return num
        else:
            #ゼロじゃなければ分割して部分水やり
            arys = div_ary(h_ary)

            for a in arys:
                num += mizuyari(a)
    return num


h_ary = []
for th in target_h:
    h_ary.append(th)
mizunum = mizuyari(h_ary)
print(mizunum)