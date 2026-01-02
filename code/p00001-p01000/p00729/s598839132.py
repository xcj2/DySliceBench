def main():
    while True:
        pc, sdt = map(int, input().split())
        if pc == 0: break
        
        rec = int(input())
        log = [[] for i in range(sdt)]
        login = []
        
        for i in range(rec):
            # 時刻　PC　生徒　ログインアウト
            t,n,m,s = map(int, input().split())

            # ログイン情報の時
            if s == 1:
                login.append([t,n,m])

            else:
                for j in range(len(login)):
                    if login[j][1] == n:
                        log[m - 1].append([login[j][0], t])
                        del login[j]
                        break

        for i in range(len(log)):
            log[i] = sorted(log[i], key = lambda x:x[0])
            log[i] = flatter(log[i], 0)

        #print("")
        #print("log::")         
        #print(log)

        qtn = int(input())

        for i in range(qtn):
            # 始まり　終わり　生徒
            ts, te, mm = map(int, input().split())
            #print("question::")
            #print(ts,te,mm)
            summ = 0

            for item in log[mm - 1]:
                #print(log[mm - 1])
                summ += usetime(item, [ts, te])

            print(summ)
            #print("")
                

def flatter(listt, fromm):
    for i in range(len(listt) - 1):
        a = listt[i]
        b = listt[i + 1]
        if b[0] <= a[1]:
            if a[1] < b[1]: a[1] = b[1]
            del listt[i + 1]
            return flatter(listt, i)

    return listt

def usetime(log,qtn):
    logs = log[0]
    loge = log[1]
    fr = qtn[0]
    to = qtn[1]

    if fr <= logs and loge <= to:
        #print("case1")
        return loge - logs
    elif logs <= fr and to <= loge:
        #print("case2")
        return to - fr
    elif logs <= fr and fr <= loge and loge <= to:
        #print("case3")
        return loge - fr
    elif fr <= logs and logs <= to and to <= loge:
        #print("case4")
        return to - logs
    else:
        #print("case0")
        return 0
main()

