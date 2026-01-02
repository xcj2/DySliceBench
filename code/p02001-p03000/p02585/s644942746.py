## coding: UTF-8

#ループ構造を見つけたらやめるところまで実装
#freshを用意して、Falseになったらやめる実装

N, K = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))



#log = [1] #訪れた地点を記録するもの
#last  = 1 #最後に訪れた地点を記録するもの（ここから次に行くところを検索する）
fresh = [False] + [True] * N #まだついたことのない場所をTrueにしている
#fresh[1] = False
#turn = ['a'] + [0] * N #なん回目におとづれたか記録する
#status = True



def search_loop(start):
    log = [start] #訪れた地点を記録するもの
    last  = start #最後に訪れた地点を記録するもの（ここから次に行くところを検索する）
    score = [C[start-1]]
    counter = 0
    while True:
        next_spot = P[last - 1]
        counter += 1
        #print(next_spot)
        if(fresh[next_spot]):
            #処理を書く
            log.append(next_spot)
            score.append(C[next_spot-1])
            last = next_spot
            fresh[next_spot] = False
            #turn[next_spot] = counter
        else:
            #log.append(next_spot)
            last = next_spot
            fresh[next_spot] = False
            #最後の人処理をする
            break
    del log[-1]
    del score[-1]
    #print('hit')
    return log, counter-1, sum(score), score
    #last, counter#turn, counter

status = True
list_loop = []
list_elements = []
list_sum = []
list_score = []

while status:
    for i in range(N+1):
        if(fresh[i]):
            #print(search_loop(i))
            a = search_loop(i)
            list_loop.append(a[0])
            list_elements.append(a[1])
            list_sum.append(a[2])
            list_score.append(a[3])
            break
        if(i == N):
            status = False

      
#print('loop', list_loop, 'elements', list_elements, 'sum', list_sum, 'score', list_score)

#print(search_loop(1))

'''
def count_sum(score,elements,start,goal):
    #歩数, 合計値でreturn
    if(start==goal):
        return 0, 0
    elif(goal > start):
        #print(score[start+1:goal+1])
        #ret = sum(score[start+1:goal+1])
        return goal-start, sum(score[start+1:goal+1])
    else:
        l = score + score
        #print(l)
        #print(l[start+1:goal+elements+1])
        return goal+elements-start, sum(l[start+1:goal+elements+1])
'''



#各ループに対して始点終点全探索
def zentansaku(loop, elements, sum, score):
    #ループを入力して、最大値を出力する
    #最終的にはループごとの最大値を出力する
    best = (-1)*(10**10)
    for start in range(elements):
        #step = 0
        now = 0
        for step in range(elements):
            #print(start, (step+start)%elements)
            #print(count_sum(score, elements, start, goal))
            #ret = (count_sum(score, elements, start, goal))
            '''
            if(start != goal):
                step += 1
                now += score[goal]
            '''
            if(step > 0):
                now += score[(step+start)%elements]
            #print('step',step, 'now',now)
            if(step > K):
                #歩きすぎ
                result = (-1)*(10**10)
            else:
                if(sum > 0):
                    #ループの合計値が正の場合、残りは歩けるだけ回る
                    available_looping = (K-step) // elements
                    #print('available_looping', available_looping)
                    result = sum * available_looping + now
                else:
                    if(step > 0):
                        result = now
                    else:
                        result = (-1)*(10**10)
            best = max(result, best)
            #print('result', result, 'best', best)
            #print(score[start:goal])
            #now = sum(score[start:goal])
    return best
            


ans = (-1)*(10**10)
for i in range(len(list_elements)):
    #print(list_loop[i], list_elements[i], list_sum[i], list_score[i])
    ans = max(ans, zentansaku(list_loop[i], list_elements[i], list_sum[i], list_score[i]))
    #print(list_loop[i], list_elements[i], list_sum[i], list_score[i], 'ans', ans)
    #print('~~~')

print(ans)