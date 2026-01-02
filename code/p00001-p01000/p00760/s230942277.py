LGE = 20
SML = 19
FUTU = 195
URUU = 200
YEAR3 = 590

def main():
    howmany = int(input())

    for i in range(howmany):
        daycount = 0
        
        dataset = input()
        dataset = dataset.split(" ")
        
        for j in range(len(dataset)):
            dataset[j] = int(dataset[j])
        #print("-------------------------------------")
        #print("data::")
        #print(dataset)
        daycount += totopmonth(dataset)
        #print("to the top of month")
        #print(daycount)
        #print("date::")
        #print(dataset)
        #print("")
        
        if dataset[0] == 1000:
            print(daycount)
        else:
            daycount += totopyear(dataset)
            #print("to the top of year")
            #print(daycount)
            #print("date::")
            #print(dataset)
            #print("")
            
            if dataset[0] == 1000:
                print(daycount)
            else:
                daycount += totheend(dataset)
                print(daycount)
                

def totopmonth(array):
    count = 0
    
    if array[2] == 1:
        return count
    elif array[0] % 3 != 0:
        if array[1] % 2 == 1:
            count = LGE - array[2] + 1
            array[2] = 1
            array[1] += 1
        else:
            count = SML - array[2] + 1
            array[2] = 1
            array[1] += 1

    else:
        count = LGE - array[2] + 1
        array[2] = 1
        array[1] += 1

    if array[1] == 11:
        array[1] = 1
        array[0] += 1
        
    return count 
        
def totopyear(array):
    count = 0
    if array[1] == 1:
        return count
    elif array[0] % 3 != 0:
        if array[1] % 2 == 1:
            count = (10 - array[1] + 1) // 2 * (LGE + SML)
            array[1] = 1
            array[0] += 1
        else:
            count = (11 - array[1] + 1) // 2 * (LGE + SML) - LGE
            array[1] = 1
            array[0] += 1
    else:
        count = (10 - array[1] + 1) * LGE
        array[1] = 1
        array[0] += 1
    return count

def totheend(array):
    count = 0
    if array[0] % 3 == 0:
        count = (999 - array[0]) // 3 * YEAR3 + URUU
        return count
    elif array[0] % 3 == 1:
        count = (999 - array[0]) // 3 * YEAR3 + YEAR3
        return count
    else:
        count = (999 - array[0]) // 3 * YEAR3 + URUU + FUTU
        return count
main()

