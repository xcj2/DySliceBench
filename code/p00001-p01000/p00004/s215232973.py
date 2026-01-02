# coding:utf-8
import sys

def determination(ls):
    return ls[0][0]*ls[1][1]-ls[0][1]*ls[1][0]

def inversion(ls):
    ret = []
    tmp = [x for x in ls]
    det = determination(tmp)
    
    if det == 0:
        return False
    else:
        tmp[0][0], tmp[1][1] = tmp[1][1], tmp[0][0]
        tmp[0][1] = tmp[0][1]*(-1)
        tmp[1][0] = tmp[1][0]*(-1)

    for x in tmp:
        ret.append(list(map(lambda x:x/det, x)))

    return ret

def dot(a,b):
    ret = []
    
    for x in a:
        ret.append(x[0]*b[0] + x[1]*b[1])

    return ret

def simueq(a,b):
    return dot(inversion(a), b)

def main():

    for line in sys.stdin:
        ls = list(map(int, line.split(' ')))
        a = [[ls[0], ls[1]], [ls[3], ls[4]]]
        b = [ls[2], ls[5]]
        
        answer = simueq(a,b)
        print('%.3f' % round(answer[0],3), '%.3f' % round(answer[1],3))
    
if __name__ == "__main__":
    main()