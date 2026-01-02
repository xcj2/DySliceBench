def nyu():
    num1,num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    #   print("x = " ,x[i]  ,"y = ",y[i])
    return num1,num2

def otoshidama(n,y):
    n = n+1
    ichiman = 0
    gosen = 0
    senen = 0
    y_tmp = y
    for i in reversed(range(n)):
#        print(i)
        ichiman  = 0
        gosen  = 0
        senen = 0
        y_tmp = y
        g_ymp = y_tmp 
        if y_tmp >= 10000*i: 
            y_tmp = y_tmp - 10000*i
            ichiman = i
            g_ymp = y_tmp
 #           if check(y_tmp,ichiman,gosen,senen) == True:
 #            return ichiman,gosen,senen
        for g in reversed(range(n-i)):
            gosen = 0
            senen = 0
            y_tmp = g_ymp
            if y_tmp >= 5000*g:
                y_tmp = y_tmp - 5000 * g
                gosen = g
#                if check(y_tmp,ichiman,gosen,senen) == True:
#                   return ichiman,gosen,senen
            senen = int(y_tmp / 1000)
            y_tmp = y_tmp % 1000
            if check(y_tmp,ichiman,gosen,senen) == True:
                return ichiman,gosen,senen
    return -1,-1,-1

def check(y_tmp,ichiman,gosen,senen):
    #print("y_tmp:",y_tmp,"ichiman:",ichiman,"gosen:",gosen,"senen:",senen,"goukei",ichiman + gosen + senen,n)
    if y_tmp == 0 and ichiman + gosen + senen  == n:
        return  True    
    return False


n,y =nyu()
num1,num2,num3 = otoshidama(n,y)
print(num1,num2,num3)

