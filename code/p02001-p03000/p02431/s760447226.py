def pushBack(vec,x):
    vec.append(x)
    return vec

def randomAccess(vec, p):
    return vec[p]

def popBack(vec):
    vec= vec[0:len(vec)-1]    
    return vec

n = int(input())
num_list = []
for i in range(n):
    num_list.append(list(map(int,input().split())))

num_of_operations = num_list[0][0]
vec = []
for i in range(len(num_list)):
    operation = num_list[i][0]
    if(operation == 2):
        vec = popBack(vec)
    else:
        n = num_list[i][1]
        
        if(operation == 0):
            vec = pushBack(vec,n)

        if(operation == 1):
            value = randomAccess(vec,n)
            print(value)
                    
