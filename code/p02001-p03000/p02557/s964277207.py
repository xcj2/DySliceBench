from collections import Counter, defaultdict
from heapq import *

class erasable_heapq:
    """
    ヒープを二本持って、本来の機能に加えて消去クエリを可能にしたもの。
    存在しない要素を消去しようとすると全体が破綻するので、注意。
    パラメータ:
        data: ヒープに入れる要素のリスト。
        allow_data_destruction: 引数で与えられたリストを破壊してよいかどうか。Trueの方が速い。
    """

    __slots__ = ["data", "to_delete"]

    def __init__(self, data, allow_data_destruction = False):
        if allow_data_destruction:
            self.data = data
        else:
            self.data = data.copy()
        heapify(self.data)
        self.to_delete = []

    def top(self):
        "最小の要素を返す。消去はしない。"
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return self.data[0]

    def push(self, elem):
        "ヒープに要素を加える。"
        heappush(self.data, elem)
    
    def pop(self):
        "最小の要素を消去して返す。"
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return heappop(self.data)

    def pushpop(self, elem):
        "ヒープにpushし、次にpopを行う、単純なpushとpopの組み合わせより高速な関数。"
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return heappushpop(self.data, elem)

    def replace(self ,elem):
        "ヒープにpopし、次にpushを行う、単純なpopとpushの組み合わせより高速な関数。"
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return heapreplace(self.data, elem)

    def erase(self, elem):
        """
        ヒープ内の要素を消去する。
        存在しない要素を消去しようとすると全体が破綻するので、注意。
        """
        heappush(self.to_delete, elem)

    def __bool__(self):
        if self.to_delete and not self.data:
            print(self.to_delete)
        while self.to_delete and self.to_delete[0] == self.data[0]:
            heappop(self.to_delete)
            heappop(self.data)
        return bool(self.data)

    def __len__(self):
        return len(self.data) - len(self.to_delete)


# greedyによる解。

# As, Bs からペアを取り除いていく操作は、
# 要素数の最大値を残り数の半分以下という状態を保存するように行える。
# つまり、
#     As = [1, 2, 3, 4]
#     Bs = [2, 2, 2, 4]
# なら、要素数の最大値である 2 の数を 
# 4, 3, 2, 1 で上から抑えながら操作を行える。
# 参考: https://twitter.com/noshi91/status/1305142205334470656?s=20

N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

As_counter = Counter(As)
Bs_counter = Counter(Bs)
all_counter = As_counter + Bs_counter

if max(all_counter.values()) > N:
    print("No")
    exit()

print("Yes")

pq = erasable_heapq([-((count << 32) + elem) for elem, count in all_counter.items()], True)

mask = (1 << 32) - 1

pair_A_to_B = defaultdict(list)
while pq:
    tmp = -pq.pop()
    count = tmp >> 32
    elem = tmp & mask

    if elem in As_counter:
        for B_elem in Bs_counter:
            if B_elem != elem:
                break
            
        # pq に変更を反映。
        if count >= 2:
            pq.push(-(((count - 1) << 32) + elem))
        pq.erase(-((all_counter[B_elem] << 32) + B_elem))
        if all_counter[B_elem] >= 2:
            pq.push(-(((all_counter[B_elem] - 1) << 32) + B_elem))
        
        # Counterに変更を反映。
        if all_counter[elem] == 1:
            del all_counter[elem]
        else:
            all_counter[elem] -= 1

        if all_counter[B_elem] == 1:
            del all_counter[B_elem]
        else:
            all_counter[B_elem] -= 1

        if As_counter[elem] == 1:
            del As_counter[elem]
        else:
            As_counter[elem] -= 1

        if Bs_counter[B_elem] == 1:
            del Bs_counter[B_elem]
        else:
            Bs_counter[B_elem] -= 1

        # AB対応を記録
        pair_A_to_B[elem].append(B_elem)

    else: # if elem not in As_counter
        for A_elem in As_counter:
            if A_elem != elem:
                break
        
        # pq に変更を反映。
        if count >= 2:
            pq.push(-(((count - 1) << 32) + elem))
        pq.erase(-((all_counter[A_elem] << 32) + A_elem))
        if all_counter[A_elem] >= 2:
            pq.push(-(((all_counter[A_elem] - 1) << 32) + A_elem))
        
        # Counterに変更を反映。
        if all_counter[elem] == 1:
            del all_counter[elem]
        else:
            all_counter[elem] -= 1

        if all_counter[A_elem] == 1:
            del all_counter[A_elem]
        else:
            all_counter[A_elem] -= 1

        if As_counter[A_elem] == 1:
            del As_counter[A_elem]
        else:
            As_counter[A_elem] -= 1

        if Bs_counter[elem] == 1:
            del Bs_counter[elem]
        else:
            Bs_counter[elem] -= 1
            
        # AB対応を記録
        pair_A_to_B[A_elem].append(elem)
       
A_ans_list = sorted(pair_A_to_B.items(), key=lambda t:t[0])
for A, ans in A_ans_list:
    print(*ans, end=' ')
