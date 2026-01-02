table = [4,1,4,1,2,1,2,1]

def round():
    item = table.pop(0)
    table.append(item)
    
def getRideNum(participants):
    rideNum = 0
    for i in range(0,8):
        n = table[i] - participants[i]
        if n >= 0:
            n = participants[i]
        else:
            n = table[i]
        rideNum += n
    return rideNum
    
def tableToNum(t):
    num = 0
    for i in range(7,-1,-1):
        n = t[i] * pow(10,7 - i)
        num += n
    return num

while(1):
    try:
        participants = list(int(x) for x in input().split())
        maxRideNum = 0
        maxTable = []

        for i in range(0,8):
            rideNum = getRideNum(participants)
            if rideNum > maxRideNum:
                maxRideNum = rideNum
                maxTable = table.copy()
                
            elif rideNum == maxRideNum:
                if tableToNum(table) < tableToNum(maxTable):
                    maxTable = table.copy()
            round()

        for i in range(0,len(maxTable)):
            if i != 0:
                print(" ",end="")
            print(maxTable[i],end="")
        print()
        
    except EOFError:
        break
