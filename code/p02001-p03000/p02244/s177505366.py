from itertools import product

def setq(ri,ci,krc):
    for ir in range(8):
        if ir!=ri:
            if krc[ir*8+ci]=="Q":
                return False,krc
            else:
                krc[ir*8+ci]="X"
    for ic in range(8):
        if ic!=ci:
            if krc[ri*8+ic]=="Q":
                return False,krc
            else:
                krc[ri*8+ic]="X"
    for ix in range(-7,7,1):
        ir=ri+ix
        ic=ci+ix
        if 0<=ir and ir<=7 and ir!=ri:
            if 0<=ic and ic<=7 and ic!=ci:
                if krc[ir*8+ic]=="Q":
                    return False,krc
                else:
                    krc[ir*8+ic]="X"
        ir=ri-ix
        ic=ci+ix
        if 0<=ir and ir<=7 and ir!=ri:
            if 0<=ic and ic<=7 and ic!=ci:
                if krc[ir*8+ic]=="Q":
                    return False,krc
                else:
                    krc[ir*8+ic]="X"
    return True,krc

def chki(i,krc):
    krc=[""]*64
    for j in range(8):
        krc[j*8+i[j]]="Q"
        bl,krc=setq(j,i[j],krc)
#        print(j,bl)
#        prk(krc)
        if not bl :
#            print(bl,i,"-------------------")
#            prk(krc)
            return False
#    print(bl,i,"-------------------")
#    prk(krc)
    return True

        
def prk(krc2):
    for i in range(8):
        print(krc2[i*8:(i+1)*8])        
    

icase=0
kr=[[] for i in range(8)]

if icase==0:
    k=int(input())
    krc=[""]*64
    for i in range(k):
        ri,ci=map(int,input().split())
        krc[ri*8+ci]="Q"
        setq(ri,ci,krc)
        kr[ri].append(ci)
elif icase==1:
    k=2
    krc=[""]*64
    ri,ci=2,2
    krc[ri*8+ci]="Q"
    setq(ri,ci,krc)
    kr[ri].append(ci)
    ri,ci=5,3
    krc[ri*8+ci]="Q"
    setq(ri,ci,krc)
    kr[ri].append(ci)
                
#prk(krc)

icnt=0

for ir in range(8):
    for ic in range(8):
        i=ir*8+ic
        if krc[i]=="":
            kr[ir].append(ic)
            
for i in product(kr[0],kr[1],kr[2],kr[3],kr[4],kr[5],kr[6],kr[7]):
    yn=""
    krc2=[""]*64
    if not chki(i,krc2):
        yn="no"
        continue
    else:
        break
if yn!="no":
    for ir in range(8):
        sti=["."]*8
        sti[i[ir]]="Q" 
        stii="".join(sti)
        print(stii)

