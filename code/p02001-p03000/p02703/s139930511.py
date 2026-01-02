#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

handler = logging.FileHandler(filename="log")
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)8s %(message)s'))
logger = logging.getLogger(__name__)
logger.addHandler(handler)

#logger.warn('hello warn')
#logger.error('hello error')
#logger.info('hello info')
#logger.debug('hello debug')


from pprint import pprint as pp
from pprint import pformat as pf
import math


from heapq import heappush, heappop
class PriorityQueue:

    def __init__(self):
        self.contaier = []

    def push(self, time, city, money):
        heappush(self.contaier, (time, (city, money)))

    def pop(self):
        time, taple = heappop(self.contaier)
        return time, taple[0], taple[1]

    def is_empty(self):
        return len(self.contaier) == 0

class Data:

    def __init__(self, money, time):
        self.money = money
        self.time = time

    def __repr__(self):
        return "money {} time {}".format(self.money, self.time)


class Path:
    def __init__(self, frm, to):
        self.frm = frm
        self.to = to

def get_line_info(num_city, num_line):
    line_info = {}
    for i in range(num_city):
        line_info[i] = {}
    for i in range(num_line):
        frm, to, money, time = map(int, input().split())
        frm -= 1
        to -= 1
        line_info[frm][to] = Data(money, time)
        line_info[to][frm] = line_info[frm][to]
    return line_info

class Person:

    def __init__(self, num_city, city_info, line_info):
        #print('city_info') # debug
        #print(city_info) # debug
        #print('line_info') # debug
        #pp(line_info) # debug
        self.city_info = city_info
        self.line_info = line_info
        self.que = PriorityQueue()
        self.dp = [None] * num_city # [city][money] = min time
        self.max_money = (50 * num_city)
        for i in range(num_city):
            self.dp[i] = [math.inf] * (self.max_money + 5)

    def travel(self, money):
        money = min(money, self.max_money)
        self.que.push(0, 0, money)
        while not self.que.is_empty():
            time, city, money = self.que.pop()
            #print('time, city, money') # debug
            #print(time, city, money) # debug
            self.exchange(time, city, money)
            self.walk_around(time, city, money)

    def exchange(self, time, city, money):
        time += self.city_info[city].time
        money += self.city_info[city].money
        self.save_and_push(time, city, money)

    def walk_around(self, time, city, money):
        for to in self.line_info[city]:
            self.walk(city, to, time, money)

    def walk(self, frm, to, time, money):
        time += self.line_info[frm][to].time
        money -= self.line_info[frm][to].money
        self.save_and_push(time, to, money)

    def save_and_push(self, time, city, money):
        if money < 0:
            return
        if not (money < len(self.dp[0])):
            return
        if time < self.dp[city][money]:
            self.dp[city][money] = time
            self.que.push(time, city, money)

    def print_ans(self):
        for city_dp in self.dp[1:]:
            print(min(city_dp))




if __name__ == '__main__':
    num_city, num_line, first_money = map(int, input().split())
    line_info = get_line_info(num_city, num_line)
    city_info = [None] * num_city
    for i in range(num_city):
        money, time = map(int, input().split())
        city_info[i] = Data(money, time)
    p = Person(num_city, city_info, line_info)
    p.travel(first_money)
    p.print_ans()






