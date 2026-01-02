import copy
def decision(a):
    #print(a)
    #print(data)
    #print(count)
    if a == 123456789:
        print(count)
        exit()
    if a in data:
        pass
    else:
        data[a] = 1
        kariokiba.append(a)
        #print(a)
        #print(data)


def str_create(i, j, h):
    h = h[:i] + h[j] + h[i+1:j] + h[i] + h[j+1:]
    #print(h)
    decision(int(h))


def create(a):
    #print(a)
    a = str(a)
    place = a.find('9')
    #print(place)
    b = c = d = e = a
    if place == 0:
        str_create(0, 1, b)
        str_create(0, 3, c)
    elif place == 1:
        str_create(0, 1, b)
        str_create(1, 2, c)
        str_create(1, 4, d)
    elif place == 2:
        str_create(1, 2, b)
        str_create(2, 5, c)
    elif place == 3:
        str_create(0, 3, b)
        str_create(3, 4, c)
        str_create(3, 6, d)
    elif place == 4:
        str_create(1, 4, b)
        str_create(3, 4, c)
        str_create(4, 5, d)
        str_create(4, 7, e)
    elif place == 5:
        str_create(2, 5, b)
        str_create(4, 5, c)
        str_create(5, 8, d)
    elif place == 6:
        str_create(3, 6, b)
        str_create(6, 7, c)
    elif place == 7:
        str_create(6, 7, b)
        str_create(4, 7, c)
        str_create(7, 8, d)
    elif place == 8:
        str_create(5, 8, b)
        str_create(7, 8, c)



tmp0 = [list(map(int, input().split())) for _ in range(3)]
data = {}
tmp1 = 0
kariokiba = []
kariokiba1 = []
for i in tmp0:
    for j in i:
        if j == 0:
            j = 9
        tmp1 *= 10
        tmp1 += j
data[tmp1] = 1
#print(data)
#print(tmp1)
tmp1 = str(tmp1)
count = 0
kariokiba.append(int(tmp1))

if tmp1 == '123456789':
    print(0)
    exit()
'''
create(tmp1)
print(kariokiba)
#print(data)

'''
while True:
    #print(kariokiba)
    kariokiba1 = copy.deepcopy(kariokiba)
    kariokiba.clear()
    count += 1
    #print(count)
    #print(data)
    for i in kariokiba1:
        create(i)


