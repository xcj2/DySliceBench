def main():
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    hp, wp = [], []
    def dfs_h(hl):
        if len(hl) == h:
            hp.append(hl)
            return
        dfs_h(hl + [0])
        dfs_h(hl + [1])
    
    def dfs_w(wl):
        if len(wl) == w:
            wp.append(wl)
            return
        dfs_w(wl + [0])
        dfs_w(wl + [1])
    
    dfs_h([])
    dfs_w([])
    
    ans = 0
    for fh in hp:
        for fw in wp:
            num = 0
            for hi, i in enumerate(fh):
                if i == 1:
                    continue
                for wi, j in enumerate(fw):
                    if j == 1:
                        continue
                    if c[hi][wi] == "#":
                        num += 1
            if num == k:
                ans += 1
    print(ans)
                    
            
            
            

if __name__ == "__main__":
    main()