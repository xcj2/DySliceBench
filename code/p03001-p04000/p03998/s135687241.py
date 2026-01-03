A = input()
B = input()
C = input()
list_A=[]
list_B=[]
list_C=[]

def cardA():
    if(not list_A):
       print("A")
    else:
        tmp = list_A.pop(0)
        if(tmp=="a"):
            cardA()
        elif(tmp=="b"):
            cardB()
        else:
            cardC()
        
def cardB():
    if(not list_B):
       print("B")
    else:
        tmp = list_B.pop(0)
        if(tmp=="a"):
            cardA()
        elif(tmp=="b"):
            cardB()
        else:
            cardC()

def cardC():
    if(not list_C):
       print("C")
    else:
        tmp=list_C.pop(0)
        if(tmp=="a"):
            cardA()
        elif(tmp=="b"):
            cardB()
        else:
            cardC()

for i in range (len(A)):
    list_A.append(A[i])

for i in range (len(B)):
    list_B.append(B[i])

for i in range (len(C)):
    list_C.append(C[i])

atmp = list_A.pop(0)
if(atmp=="a"):
    cardA()
elif(atmp=="b"):
    cardB()
else:
    cardC()
