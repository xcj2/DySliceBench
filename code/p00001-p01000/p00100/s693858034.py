# coding: utf-8
# Here your code !
employeeSalesList = []

def resetDataset():
    del employeeSalesList[0 : len(employeeSalesList) + 1]

def readDataCount():
    return int(input())

def searchEmployeeSales(employeeId):
    for data in employeeSalesList:
        if data[0] == employeeId:
            return data
    
    newData = [employeeId, 0]
    employeeSalesList.append(newData)
    return newData

def printEmployeeOfDataset():
    answerList = [data[0] for data in employeeSalesList if data[1] >= 1000000]
    if len(answerList) == 0:
        print("NA")
    else:
        print("\n".join(map(str, answerList)))

resetDataset()
dataCount = readDataCount()
while dataCount > 0:
    for _ in range(dataCount):
        employeeId, price, volume = list(map(int, input().split(" ")))
        employeeSales = searchEmployeeSales(employeeId)
        employeeSales[1] += price * volume
    printEmployeeOfDataset()
    resetDataset()
    dataCount = readDataCount()