#-*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B
"""
import itertools
import time
import logging

def input_from_txt(number=1):
    import requests
    url = "https://judgedat.u-aizu.ac.jp/testcases/ALDS1_11_B/%s/in" % number
    res = requests.get(url)
    input = res.text.split("\n")
    n = int(input[0])
    Ss = []
    for i in range(n):
        S = list(map(int, input[1+i].split()))
        Ss.append(S)
    return (n, Ss)

def input_array():
    n = int(input())
    Ss = []
    for i in range(n):
        S = list(map(int, input().split()))
        Ss.append(S)
    return (n, Ss)

def show_matrix(n, Ss):
    for i in range(n):
        vth = Ss[i][0]
        vd = Ss[i][1]
        adjs = Ss[i][2:]
        row = []
        for j in range(1, 1+n):
            if j in adjs: row.append(1)
            else: row.append(0)
        logging.info(" ".join(map(str, row)))

class Verticies:
    def __init__(self, id, value, degree, adjs:list):
        self.id = id
        self.value = value
        self.degree = degree
        self.d = 0 # timesamp
        self.f = 0 # timesamp
        self.adjs = adjs

    def visit(self, ts):
        logging.debug("miso0a: visiting id(%s)" % self.id)
        if not self.is_visited():
            self.d = ts
            logging.debug("visited id(%s) and ts stamped as %s" % (self.id, ts))
            logging.info("id:%s d:%s f:%s (preorder)" % (self.id, self.d, self.f))
            ts+=1
            logging.debug("miso1: ts incremented as %s" % ts)
        return ts

    def all_visit(self, ts):
        if self.adjs_all_visited() and not self.adjs_all_stamped():
            self.f = ts
            logging.info("id:%s d:%s f:%s (=================)" % (self.id, self.d, self.f))
            ts +=1
        return ts

    def is_visited(self):
        logging.debug ("miso9: id(%s) is_visited: %s(%s)" % (self.id, not self.d == 0, self.d))
        return (not self.d == 0)

    def adjs_all_visited(self):
        visited = [v.is_visited() for v in self.adjs]
        logging.debug("miso5: %s" % self.adjs)
        logging.debug("miso(visited): %s" % visited)
        completed = all(visited)
        logging.debug("miso(completed): %s" % completed)
        return completed

    def adjs_all_stamped(self):
        stamped = [v.f != 0 for v in self.adjs]
        logging.debug("--- miso5 ---: %s" % [x.f for x in self.adjs])
        logging.debug("miso(stamped): %s" % stamped)
        completed = all(stamped)
        logging.debug("miso(completed): %s" % completed)
        return completed

    def get_adjs_info(self):
        return zip([v.id for v in self.adjs], [v.f for v in self.adjs])




def instanciate_vertex(V:list):
    vertex = {}
    for v in V:
        id = int(v[0])
        degree = v[1]
        adjs = v[2:]
        vertices = Verticies(id, 0, degree, adjs)
        vertex[id] = vertices
    # switch from string to Instance
    for id, vertices in vertex.items():
        vertex[id].adjs = [ vertex[i] for i in vertex[id].adjs]
    # sort by young id ascendence
    return sorted(list(vertex.values()), key=lambda v: v.id)


ANSWER={}
def dfs(v: Verticies, ts, stack:list):
    logging.info("dfs(v.id:%s, ts:%s, stack:%s)" % (v.id, ts, [ x.id for x in stack]))
    if not v.is_visited():
        ts = v.visit(ts)

    if len(v.adjs) == 0 or (v.adjs_all_visited()):
        v.f = ts
        logging.warn("id:%s d:%s f:%s (=================)" % (v.id, v.d, v.f))
        ANSWER[v.id] = (v.id, v.d, v.f)
        ts +=1
        stack.pop()
    else:
        logging.info("adjs_info:%s= (========not yet =======)" % ([(a,b) for a, b in v.get_adjs_info()] ))

    for next_v in v.adjs:
        if not next_v.is_visited():
            stack.append(next_v)
            break
    # ts = v.visit(ts)
    # ts = v.all_visit(ts)

    return ts

def dfs_all(vertex:list):
    stack = []
    #stack.append(vertex[0])
    ts = 1
    fin = False
    while not fin:
        for i, v in enumerate(vertex):
            logging.info("i:%s == len(vertex)-1: %s" % ( i, len(vertex)-1))
            if not v.is_visited():
                stack.append(v)
                break
            if i == len(vertex)-1: fin = True
        while len(stack) > 0:
            v = stack[len(stack)-1]
            ts = dfs(v, ts, stack)
            logging.info("while stack non empty")
            #time.sleep(1)
        logging.info("while True")
        #time.sleep(1)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.ERROR)
    #mode = "test"
    mode = "prod"
    if mode == "test":
        (n, Ss) = input_from_txt(1)
        show_matrix(n, Ss)
        logging.getLogger().setLevel(logging.INFO)
        #logging.getLogger().setLevel(logging.DEBUG)
    else:
        (n, Ss) = input_array()

    vertex = instanciate_vertex(Ss)
    logging.debug(vertex)
    dfs_all(vertex)
    from collections import OrderedDict
    for id, d, f in OrderedDict(sorted(ANSWER.items())).values():
        print("%s %s %s" % (id, d, f))
    #dfs_all(vertex)



