N = str(input())

resultdist = {}

ketalist = [1,11,111,1111,11111]

def chukan(N):
    if(len(N) > 2):
        return int(N[1:-1])
    else:
        return 0

def retketa1(N):
    if(len(N) > 1):
        return ketalist[len(N)-2]
    else:
        return 0

def retketa2(N):
    if(len(N) > 2):
        return ketalist[len(N)-3]
    else:
        return 0

for i in range(1,10):
    for j in range(1,10):
        count = 1 if i==j else 0
        if(i < int(N[0])):
            count += retketa1(N)
        if(i > int(N[0])):
            count += retketa2(N)
        if(i == int(N[0])):
            count += retketa2(N)
            if(j > int(N[-1])):
                count += chukan(N)
            else:
                if(len(N) > 1):
                    count += chukan(N) + 1
                else:
                    count += chukan(N)

        resultdist[str(i)+str(j)] = count

resulutcount = 0

for i in range(1, int(N)+1):
    l = str(i)[0]
    f = str(i)[-1]
    if(f != "0"):
        resulutcount += resultdist[f+l]
print(resulutcount)