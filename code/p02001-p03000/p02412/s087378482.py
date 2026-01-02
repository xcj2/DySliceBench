# coding: utf-8
# Here your code !

def func():
    data=[]
    while(True):
        try:
            line=[ int(item) for item in input().rstrip().split(" ") ]
            if(line == [0,0]):
                break
            data.append(line)
        except EOFError:
            break
        except:
            return inputError()
    
    left=1
    numbers=3
    [print(len(sumcombination(left,line[0],numbers,line[1]))) for line in data]

def sumcombination(left,right,numbers,total):
    '''
    left ~ right??????????????°??????(numbers)????????´??°???????¨????total?????????????????????????????????????????????
    '''
    result=[]
    if(numbers==1):
        if( (left <= total) and (right >= total) ):
            result=[total]
        return(result)
    
    for i in range(left,right+1):
        if( numbers == 2):
            if(i >= total-i):
                break
            elif( (i != total-i) and (left <= total-i) and (right >= total-i) ):
                result.append([i,total-i])
        elif( ( len( range(i,right+1) ) < numbers ) or ( sum( range(i+1,i+numbers) ) > total-i ) ):
            break
        elif( sum( range(right-numbers+2,right+1) ) < total-i ):
            continue
        else:
            sub = sumcombination(i+1,right,numbers-1,total-i)
            if(len(sub)>0):
                [items.insert(0,i) for items in sub]
                result.extend(sub)

    return(result)

def inputError():
    print("input error")
    return -1

func()