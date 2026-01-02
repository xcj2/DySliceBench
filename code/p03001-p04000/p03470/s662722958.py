def nyu():
    num1 = input()
    num1 = int(num1)
    #num2 = int(num2)
    return num1

def nyu2(n):
    tmp =[]
    for i in range(n):
        tmp.append(int(input()))
    return tmp

def sort(mochi):
    tmp_mochi = 0
    for i in range(n):
        for k in range(n):
            if mochi[i]>mochi[k] :
                tmp_mochi = mochi[i]
                mochi[i] = mochi[k]
                mochi[k] = tmp_mochi
    return mochi

def check(mochi):
    max =101
    cnt =0

    for i in range(n):
        if max>mochi[i]:
            max = mochi[i]
            cnt +=1
    return cnt

n=nyu()
mochi = nyu2(n)
mochi = sort(mochi)
print(check(mochi))