def judge(p, r, l):
    rowBorder = r
    highBorder = l -r
    ret = False
    if p <= highBorder and p >= rowBorder:
        ret = True
    
    return ret

def circleinRec(w, h, x, y, r):
    #W
    retW = judge(x, r, w)

    #H
    retH = judge(y, r, h)

    if retW == True and retH == True:
        return True

    else:
        return False

def main():
    val = input().split()
    val = [int(n) for n in val]
    ret = circleinRec(val[0], val[1], val[2], val[3], val[4])
    if ret == True:
        print('Yes')

    else:
        print('No')

if __name__ == '__main__':
    main()
