import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001


class Node:
    def __init__(self):
        self.parent_id = -1
        self.children = [-1]*128
        self.suffix_link = -1
        self.finish_FLG = False


class Info:
    def __init__(self,arg_node_id,arg_ch):
        self.node_id = arg_node_id
        self.ch = arg_ch


class StringSearch:
    def __init__(self,arg_Pattern):
        self.Pattern = arg_Pattern
        self.root = 0
        self.index = 1
        self.nodes = []
        for _ in range(len(self.Pattern)+1):
            self.nodes.append(Node()) #★★★★★★appendしないと、build()が上手く動かない(2019/11/10)★★★★★★

    def build(self):
        self.nodes[self.root].suffix_link = -1
        #トライ木のノードを初期化
        for i in range(len(self.Pattern)+1):
            self.nodes[i].parent_id = -1
            self.nodes[i].finish_FLG = False
            for k in range(128):
                self.nodes[i].children[k] = -1

        #トライ木を構築する
        tmp_index = 0
        tmp_ch = ord(self.Pattern[tmp_index])

        tmp_loc = self.root


        while True:

            parent_id = tmp_loc

            self.nodes[tmp_loc].children[tmp_ch] = self.index #パターン文字列が1種類なので、機械的にノード追加(インデックスを増やす)
            self.index += 1
            #子ノードに移動
            tmp_loc = self.nodes[tmp_loc].children[tmp_ch]
            self.nodes[tmp_loc].parent_id = parent_id

            tmp_index += 1

            if tmp_index == len(self.Pattern):
                self.nodes[tmp_loc].finish_FLG = True
                break

            tmp_ch = ord(self.Pattern[tmp_index])

        #Suffix_linkを構築する
        MAKE_SL = deque()
        for i in range(128):
            if self.nodes[self.root].children[i] != -1:
                node_id = self.nodes[self.root].children[i]
                self.nodes[node_id].suffix_link = self.root #root直下のsuffix_linkは必ずrootなので、MAKE_SLには突っ込まない
                for k in range(128):
                    if self.nodes[node_id].children[k] != -1:
                        MAKE_SL.append(Info(self.nodes[node_id].children[k],k)) #ノードのidと、最後の経路をpushする

        while len(MAKE_SL) > 0:
            info = MAKE_SL.popleft()
            node_id = info.node_id #新たにsuffix_linkを張りたいノードのid
            tmp_ch = info.ch #ノードの文字

            for i in range(128):
                if self.nodes[node_id].children[i] != -1:
                    MAKE_SL.append(Info(self.nodes[node_id].children[i],i)) #続く経路があれば、先にappendておく

            #親のsuffix_link先は、自分のsuffix_link先のprefixになっているので、親のsuffix_link情報を利用する
            tmp_loc = self.nodes[self.nodes[node_id].parent_id].suffix_link
            while tmp_loc != self.root:
                if self.nodes[tmp_loc].children[tmp_ch] != -1: #ノードの文字へと繋がる経路あり
                    break
                tmp_loc = self.nodes[tmp_loc].suffix_link #なければ遡る

            if tmp_loc == self.root:
                if self.nodes[self.root].children[tmp_ch] != -1:
                    self.nodes[node_id].suffix_link = self.nodes[self.root].children[tmp_ch]
                else:
                    self.nodes[node_id].suffix_link = self.root
            else:
                self.nodes[node_id].suffix_link = self.nodes[tmp_loc].children[tmp_ch]

    def search(self,T):
        #T上の文字を走査する
        tmp_loc = self.root
        for i in range(len(T)):
            tmp_ch = ord(T[i])

            if self.nodes[tmp_loc].children[tmp_ch] != -1: #次の文字が繋がる場合
                tmp_loc = self.nodes[tmp_loc].children[tmp_ch] #次のノードに移動する

                if self.nodes[tmp_loc].finish_FLG == True:
                    print("%d"%(i-len(self.Pattern)+1))
                    tmp_loc = self.nodes[tmp_loc].suffix_link

            else: #次の文字と一致しない場合→suffix_linkを辿る

                if tmp_loc == self.root:
                    continue

                tmp_loc = self.nodes[tmp_loc].suffix_link
                while tmp_loc != self.root:
                    if self.nodes[tmp_loc].children[tmp_ch] != -1:
                        break
                    tmp_loc = self.nodes[tmp_loc].suffix_link

                if self.nodes[tmp_loc].children[tmp_ch] != -1: #tmp_chへと繋がるノードに辿り着いた場合
                    tmp_loc = self.nodes[tmp_loc].children[tmp_ch]
                    #少なくとも1文字遡るので、ここでfinish_FLGがtrueになることはない
                else:
                    pass #tmp_loc == rootであるはず

T = input()
P = input()

string_search = StringSearch(P)
string_search.build()
string_search.search(T)

