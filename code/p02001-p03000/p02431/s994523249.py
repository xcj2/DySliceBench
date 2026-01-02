numberOfQuery=int(input())
count=0
listForStock=[]
listForPrint=[]

def popBack():
    lastIndex=len(listForStock)-1
    del listForStock[lastIndex]

def pushBack(x):
    listForStock.append(x)

def randomAccess(p):
    listForPrint.append(listForStock[p])

#-----------------main--------------------
while count<numberOfQuery:
    query=input()
    if query=="2":
        popBack()
    else:
        querys=query.split()
        if querys[0]=="0":
            pushBack(int(querys[1]))
        elif querys[0]=="1":
            randomAccess(int(querys[1]))
        else:
            print("入力が不正です")
            break
    count+=1

for chip in listForPrint:
    print(chip)
#-----------------main--------------------
