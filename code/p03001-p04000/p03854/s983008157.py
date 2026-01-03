import sys
sys.setrecursionlimit(10**6)
g=[]

def  jdream(l,i):
    if len(l)>=i+5:

        if l[i:i+5]=="dream":
            i=i+5
            if i==len(l):
                g.append("Y")
                return
     
            else:
                jer(l,i)
                jdream(l,i)
                return
        else:
            
            return
    else:
        
        return

def jerase(l,i):
    if len(l)>=i+5:

        if l[i:i+5]=="erase":
            i=i+5
            if i==len(l):
                g.append("Y")
                return
            else:
                jr(l,i)
                jerase(l,i)
                jdream(l,i)
                return
        else:
            
            return
    else:
        
        return

def jer(l,i):
    if len(l)>=i+2:

        if l[i:i+2]=="er":
            i=i+2
            if i==len(l):
                g.append("Y")
                return
            else:
                jase(l,i)
                jerase(l,i)
                jdream(l,i)
                return
        else:
            
            return
    else:
        
        return

def jase(l,i):
    if len(l)>=i+3:

        if l[i:i+3]=="ase":
            i=i+3
            if i==len(l):
                g.append("Y")
                return
            else:
                jdream(l,i)
                jerase(l,i)
                jr(l,i)
                return
        else:
            
            return
    else:
        
        return

def jr(l,i):
    if len(l)>=i+1:

        if l[i:i+1]=="r":
            i=i+1
            if i==len(l):
                g.append("Y")
                return
            else:
                jdream(l,i)
                jerase(l,i)
                return
        else:
            
            return

    else:
        
        return

s=input()
n=0
jerase(s,n)
n=0
jdream(s,n)


if 'Y' in g:
    print("YES")
else:
    print("NO")