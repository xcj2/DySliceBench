K=int(input())

G=[1,2,3,4,5,6,7,8,9]

def Judge1(number):
    letter=str(number)
    judge=1
    if number==1:
        judge=0
    elif letter[0]!='1':
        judge=0
    else:
        for i in range(1,len(letter)):
            if letter[i]!='0':
                judge=0
                break 
    return judge

def Judge9(number):
    letter=str(number)
    judge=1
    for i in range(len(letter)):
        if letter[i]!='9':
            judge=0
            break
    return judge

def generate(number):
    if Judge1(number)==1:
        return [number*10,number*10+1]
    elif Judge9(number)==1:
        return [number*10+8,number*10+9]
    else:
        letter=str(number)
        newnumber=int(letter+letter[-1])
        return [newnumber-1,newnumber,newnumber+1]

def Generate(L):
    A=[]
    for i in range(len(L)):
        A.extend(generate(L[i]))
    return A

def check(number):
    letter=str(number)
    judge=1
    for i in range(len(letter)-1):
        if abs(int(letter[i])-int(letter[i+1]))>1:
            judge=0
            break
    return judge

Ans=[G]
ANS=[1,2,3,4,5,6,7,8,9]
for x in range(9):
    N=Generate(Ans[-1])
    NN=[]
    for y in range(len(N)):
        if check(N[y])==1:
            NN.append(N[y])
    Ans.append(NN)
    ANS.extend(NN)


#print(Ans)
#print(LastANS)
#print(len(ANS))
print(ANS[K-1])





    

    
