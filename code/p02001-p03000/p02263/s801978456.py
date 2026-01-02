import sys

def GetReadlineData():
    readlinedata= sys.stdin.readline()
    splitdata = [i for i in readlinedata.split()]
    
    return splitdata
            
def CalcShapingData(splitdata):

    calcresult = [0 for i in range(len(splitdata))]

    j = 0
    for i in range(0, len(splitdata)):
        if splitdata[i].isdecimal():
            j = j + 1
            calcresult[j] = int(splitdata[i])
            result = int(splitdata[i])
            #if j == 2:
                #print('{}:{}'.format(j,calcresult[j]))
        else:
            #print(splitdata[i])
            if splitdata[i] == '+':
                result = calcresult[j-1] + calcresult[j]
                #print(calcresult[j-2])
                #print(calcresult[j-1])
                #print(result)
                j = j - 1
            elif splitdata[i] == '-':
                result = calcresult[j-1] - calcresult[j]
                #print(calcresult[j-1])
                #print(calcresult[j])
                #print(result)
                j = j - 1
            elif splitdata[i] == '*':
                result = calcresult[j-1] * calcresult[j]
                #print(calcresult[j-1])
                #print(calcresult[j])
                #print(result)
                j = j - 1
            elif splitdata[i] == '/':
                result = int(calcresult[j-1]) / int(calcresult[j])
                #print(result)
                j = j -1
            
            #calcresult.pop(j-1)
            #calcresult.pop(j)
            #print(j)
            calcresult[j] = result

    for k in range(1,j):
        calcresult.pop(k)

    return result


def main():
    splitdata = GetReadlineData()
    result = CalcShapingData(splitdata)
    print(result)

if __name__ == '__main__':
    main()
