def readinput():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    return (a,b,c,x)

def main(a,b,c,x): 
    result = []
    for na in range(a+1):
        residue = x - 500*na
        if (residue < 0):
            break
        for nb in range(b+1):
            residue = x - 500*na - 100*nb
            if(residue < 0):
                break
            nc = residue // 50
            if (nc > c):
                break
            result.append((na,nb,nc))
    return result

def main_(a,b,c,x): 
    result = []
    for na in range(a+1):
        residue = x - 500*na
        if (residue < 0):
            break
        for nb in range(b+1):
            residue = x - 500*na - 100*nb
            if(residue < 0):
                break
            nc = residue // 50
            if (nc > c):
                continue
            result.append((na,nb,nc))
    return result

def main2(a,b,c,x):
    result = []
    for na in range(a+1):
        for nb in range(b+1):
            for nc in range(c+1):
                if (500*na+100*nb+50*nc == x):
                    result.append((na,nb,nc))
                    break
    return result

def main3(a,b,c,x):
    result = []
    for na in range(a+1):
        for nb in range(b+1):
            res = x - na*500 - nb*100
            nc = res // 50
            if (0<= nc and nc <= c):
                result.append((na,nb,nc))
                continue
    return result

if __name__ == '__main__':
    a,b,c,x = readinput()
#    result=main(a,b,c,x)
    result=main_(a,b,c,x)
    for res in result:
        (na,nb,nc)=res
#        print(res)
#        print(na*500+nb*100+nc*50)
    print(len(result))
