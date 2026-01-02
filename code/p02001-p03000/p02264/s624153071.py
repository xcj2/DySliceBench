def readinput():
    n,q = list(map(int,input().split()))
    procs = []
    for i in range(n):
        name, strtime = input().split()
        inttime = int(strtime)
        procs.append([name, inttime])
    return n,q,procs

def dispach(t, q, procs):
    t0 = t
    #print(t0, t, procs)

    proc = procs.pop(0)
    procname = proc[0]
    tremain = proc[1]
    if (tremain > q):
        proc[1] = tremain - q
        procs.append(proc)
        t0 += q
    else:
        t0 += tremain
        print(procname+' '+str(t0))

    #print(t0, t, procs)
    return t0

def main(n,q,procs):
    t = 0
    #print(procs)
    while(len(procs)>0):
        t = dispach(t, q, procs)
        #print(t, procs)
    return

if __name__=='__main__':
    n,q,procs=readinput()
    #print(procs)
    main(n,q,procs)

