def hash1(m, key):
    return key % m

def hash2(m, key):
    return 1 +  key % (m - 1)

def hash(m, key, i):
    return (hash1(m, key) + i * hash2(m, key) ) % m

def insert(T, key):
    i = 0
    l = len(T)
    while True:
        h = hash(1046527,key,i)
        if (T[h] == None ):
            T[h] = key
            return h
        elif (T[h] == key):
            return h
        else:
            i += 1

def search(T,key):
    l = len(T)
    i = 0
    while True:
        h = hash(1046527,key,i)
        if(T[h] == key):
            return h
        elif(T[h] is None or h >= l):
            return -1
        else:
            i += 1

def find(T, key):
    a = search(T,key)
    if(a == -1):
        print('no')
    else:
        print('yes')

dict = {'A' : '1', 'C' : '2', 'G' : '3', 'T' : '4'}
data = []
T = [None]*1046527
n = int(input())


while n > 0:
    st = input()
    d = list(st.split())

### convert key to num(1~4)
    tmp_key = ''
    for x in list(d[1]):
        tmp_key += dict[x]

    data.append([d[0],int(tmp_key)])
    n -= 1
for com in data:
    if(com[0] == 'insert'):
        insert(T,com[1]) 
    else:
        find(T,com[1])