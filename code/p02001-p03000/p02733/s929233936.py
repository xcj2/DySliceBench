def can_merge(K: int, prev_cnt: list, cur_cnt: list) -> bool:
    ret = True
    for i, _ in enumerate(cur_cnt):
        if prev_cnt[i] + cur_cnt[i] > K:
            ret = False
            break
    return ret

def merge(prev_cnt: list, cur_cnt: list):
    for i, _ in enumerate(cur_cnt):
        prev_cnt[i] += cur_cnt[i]

def main():
    H, W, K = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())

    min_split_num = 999+9
    for hbitv in range(2**(H-1)):
        split_num = bin(hbitv).count('1')
        region_num = split_num + 1
        prev_cnt = [0] * region_num

        # ->
        for w in range(W):
            impossible_hbitv = False
            cur_cnt = [0] * region_num

            # |
            # v
            ri = 0
            for h in range(H):
                if S[h][w] == '1':
                    cur_cnt[ri] += 1
                    if cur_cnt[ri] > K:
                        impossible_hbitv = True
                        break

                if (hbitv >> h) % 0b10 == 1:
                    ri += 1

            if impossible_hbitv:
                break

            if can_merge(K, prev_cnt, cur_cnt):
                merge(prev_cnt, cur_cnt)
            else:
                split_num += 1
                prev_cnt, cur_cnt = cur_cnt, prev_cnt
        
        if not impossible_hbitv:
            min_split_num = min(min_split_num, split_num)

    print(min_split_num)
            
if __name__ == '__main__':
    main()
