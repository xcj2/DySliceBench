def J(m) :
    tmp = m[-1]
    del m[-1]
    m.insert(0, tmp)
    return m
    
def C(m) :
    tmp = m[0]
    del m[0]
    m.append(tmp)
    return m
    
def E(m) :
    if len(m) % 2 == 1 :
        x = len(m) // 2
        tmp = m[0:x]
        middle = m[x]
        del m[0:x+1]
        m = m + [middle] + tmp
        return m
    
    else :
        x = len(m) // 2
        tmp = m[0:x]
        del m[0:x]
        m = m + tmp
        return m
    
def A(m) :
    m.reverse()
    return m
    
def M(m) :
    for i in range(len(m)) :
        if '0' <= m[i] <= '8' :
            m[i] = str(int(m[i]) + 1)
        elif m[i] == '9' :
            m[i] = '0'
    return m
    
def P(m) :
    for i in range(len(m)) :
        if '1' <= m[i] <= '9' :
            m[i] = str(int(m[i]) - 1)
        elif m[i] == '0' :
            m[i] = '9'
    return m

n = int(input())
for i in range(n) :
    member = list(input())
    member.reverse()
    message = list(input())
    
    for j in range(len(member)) :
        if member[j] == 'J' :
            message = J(message)
        elif member[j] == 'C' :
            message = C(message)
        elif member[j] == 'E' :
            message = E(message)
        elif member[j] == 'A' :
            message = A(message)
        elif member[j] == 'P' :
            message = P(message)
        elif member[j] == 'M' :
            message = M(message)
    print(*message, sep='')
            
