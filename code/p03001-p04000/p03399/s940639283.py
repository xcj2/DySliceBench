#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import re
import heapq
import sys

source="""
ちょくちょくちょく　ちょくだいちょくだい　ちょく　だいだい
    ちょくだいちょく　電車きっぷ
    ちょくだいちょく　電車乗り放題
    ちょくだいちょく　バスきっぷ
    ちょくだいちょく　バス乗り放題
    ちょくちょく　合計　ちょく だいだい
    だいだいだいだい　だいだいだいだいだい 電車きっぷ 電車乗り放題
        ちょくちょく　合計　ちょくちょくちょくちょく 合計 電車乗り放題
    だいだいだいちょく　ちょく だいちょく
        ちょくちょく　合計　ちょくちょくちょくちょく 合計 電車きっぷ
    だいだいちょくだい

    だいだいだいだい　だいだいだいだいだい バスきっぷ バス乗り放題
        ちょくちょく　合計　ちょくちょくちょくちょく 合計 バス乗り放題
    だいだいだいちょく　ちょく だいちょく
        ちょくちょく　合計　ちょくちょくちょくちょく 合計 バスきっぷ
    だいだいちょくだい
    だいちょく 合計

ちょくちょくだい

"""

def main():
    commands=re.split('[\r\n 　]',source)
    commands = [x for x in commands if x!='']

    interpreter = Interpreter(commands)
    interpreter.Run()


class Stack:
    def __init__(self):
        self.stack = []
    def __len__(self):
        return len(self.stack)
    def Push(self, e):
        self.stack.append(e)
    def Peek(self):
        try:
            return self.stack[-1]
        except IndexError:
            print('\nError Message:\n\tThere is no element in the stack!\n')

    def Pop(self):
        try:
            sEl = self.stack.pop()
            return sEl
        except IndexError:
            print('\nError Message:\n\tThere is no element in the stack!\n')

class Queue:
    def __init__(self):
        self.queue = []
    def __len__(self):
        return len(self.queue)

    def Enqueue(self, e):
        self.queue.append(e)

    def Dequeue(self):
        try:
            qEl = self.queue[0]
            del self.queue[0]
            return qEl
        except IndexError:
            print ('\nError Message:\n\tThere is no element in the queue!\n')

class Deque:
    def __init__(self):
        self.data=[]
    def __len__(self):
        return len(self.data)
    def PopFront(self):
        try:
            qEl = self.data[0]
            del self.data[0]
            return qEl
        except IndexError:
            print ('\nError Message:\n\tThere is no element in the queue!\n')
    def PopBack(self):
        try:
            qEl = self.data[-1]
            del self.data[-1]
            return qEl
        except IndexError:
            print ('\nError Message:\n\tThere is no element in the queue!\n')
    def PushFront(self,val):
        self.data.insert(0,val)
    def PushBack(self,val):
        self.data.append(val)

class PriorityQueue:
    def __init__(self):
        self.data=[]
    def Pop():
        return heapq.heappop(self.data)
    def Push(val):
        heapq.heappush(self.data,val)
    def __len__(self):
        return len(self.data)

class Function:
    pass

# プリミティブな関数
class PrimitiveFunction(Function):
    def __init__(self,_arg_num, _func):
        self.arg_num = _arg_num
        self.func = _func

    def Run(self,args):
        return self.func(args)


class Interpreter:

    def __init__(self,_commands):
        self.commands = _commands
        self.vars = {}
        self.funcs = {}
        self.input_que = Queue()

        self.funcs["ちょくちょくちょくちょく"]= PrimitiveFunction(2, lambda a : a[0] + a[1]) # 加算
        self.funcs["ちょくちょくちょくだい"]=   PrimitiveFunction(2, lambda a : a[0] - a[1]) # 減算
        self.funcs["ちょくちょくだいちょく"]=   PrimitiveFunction(2, lambda a : a[0] * a[1]) # 乗算
        self.funcs["ちょくちょくだいだい"]=     PrimitiveFunction(2, lambda a : a[0] / a[1]) # 除算
        self.funcs["ちょくちょくだいだいだい"]= PrimitiveFunction(2, lambda a : a[0] % a[1]) # 余剰演算
        self.funcs["だいだいだいだいだい"]=     PrimitiveFunction(2, lambda a : self.BoolToInt(a[0] > a[1])) # 大なり
        self.funcs["だいだいだいだいちょく"]=   PrimitiveFunction(2, lambda a : self.BoolToInt(a[0] == a[1])) # イコール

    # 関数を定義する
    def DefFunc(self,name,commands):
        udf = UserDefinedFunction(self, commands)
        self.funcs[name]= udf


    # 空白で区切られた文字の読み込み
    def ReadStr(self):
        if (len(self.input_que) == 0):
            read = input()
            inputs = read.split()
            for s in inputs:
                self.input_que.Enqueue(s)
        return self.input_que.Dequeue()

    # bool型をint型に変換
    def BoolToInt(self,a):
        return 1 if a else 0

    def Run(self):
        self.now_index = 0
        while (self.now_index < len(self.commands)):
            command = self.commands[self.now_index]
            self.now_index+=1

            if (command == "ちょくちょくちょく"):
                func_begin = self.now_index
                func_name = self.commands[self.now_index]
                while (self.now_index < len(self.commands) and not(self.commands[self.now_index] == "ちょくちょくだい" and not(self.commands[self.now_index - 1] == "ちょく" or self.commands[self.now_index - 1] == "だい"))):
                    self.now_index+=1
                func_end = self.now_index
                func_commands = self.commands[func_begin:func_end+1]
                self.DefFunc(func_name, func_commands)

        self.funcs["ちょくだいちょくだい"].Run(None)

# ユーザー定義関数
class UserDefinedFunction(Function):
    def __init__(self,_interpreter,_commands):
        self.interpreter = _interpreter
        self.commands = _commands
        self.ifs = {}
        whiles = {}

        self.now_index = 1
        self.arg_num = int(self.GetInt())

        self.now_index += self.arg_num

        if_stack = Stack()
        while_stack = Stack()

        while (self.now_index < len(self.commands)):
            command = self.commands[self.now_index]
            if (command == "だいだいだいだい" and self.commands[self.now_index - 1] != "ちょく" and self.commands[self.now_index - 1] != "だい"): # if
                if_stack.Push(Queue())
                if_stack.Peek().Enqueue(self.now_index)
            elif (command == "だいだいだいちょく" and self.commands[self.now_index - 1] != "ちょく" and self.commands[self.now_index - 1] != "だい"): # elif
                if_stack.Peek().Enqueue(self.now_index)
            elif (command == "だいだいちょくだい" and self.commands[self.now_index - 1] != "ちょく" and self.commands[self.now_index - 1] != "だい"): # end if
                end = self.now_index
                que = if_stack.Peek()
                fst = que.Dequeue()
                while (len(que) != 0):
                    snd = que.Dequeue()
                    self.ifs[fst]=(snd, end)
                    fst = snd
                self.ifs[fst]=(end, end)
            elif (command == "だいだいちょくちょく" and self.commands[self.now_index - 1] != "ちょく" and self.commands[self.now_index - 1] != "だい"): # while
                while_stack.Push(self.now_index)
            elif (command == "だいちょくだいちょく" and self.commands[self.now_index - 1] != "ちょく" and self.commands[self.now_index - 1] != "だい"): # end while
                begin = while_stack.Pop()
                end = self.now_index
                whiles[begin]=end
            self.now_index+=1

    # Getxxのself.now_indexは終了時、xxを表すコマンドの直後のindexに変更される
    def GetInt(self):
        ret = 0
        self.now_index+=1
        s = self.commands[self.now_index]
        i = (3 if s[0] == 'ち' else 2)
        while (i < len(s)):
            ret *= 2
            if (s[i] == 'ち'):
                ret+=1
                i += 3
            else:
                i += 2
        if (s[0] == 'ち'):
            ret *= -1
        self.now_index+=1
        return ret

    def GetChar(self):
        ret = 0
        i = 0
        self.now_index+=1
        s = self.commands[self.now_index]
        while (i < len(s)):
            ret *= 2
            if (s[i] == 'ち'):
                ret+=1
                i += 3
            else:
                i += 2
        self.now_index+=1
        return chr(ret)
    def GetStr(self):
        self.now_index+=1

        # 文字数読み込み
        len = int(self.GetVal()) # 文字列の長さ

        # 文字読み込み
        s = ""
        for i in range(len):
            ch = self.GetVal()
            s += ch
        return s
    def GetList():
        self.now_index+=1

        len = self.GetVal()

        list = []
        for i in range(len):
            list.append(self.GetVal())
        return list

    # 任意の値を取得する 通常はこれを使う
    def GetVal(self):
        command = self.commands[self.now_index]
        if (command == "ちょく"):
            return self.GetInt()
        elif (command == "ちょくだい"):
            return self.GetList()
        elif (command == "だい"):
            return self.GetChar()
        elif (command == "だいだい"):
            return self.GetStr()
        elif (command == "だいだいちょくだいだい"): # deque構築
            self.now_index+=1
            return Deque()
        elif (command == "だいちょくだいちょくだい"): # priority_queue構築
            self.now_index+=1
            return PriorityQueue()
        elif (command == "だいちょくちょく"): # リストの要素数を求める
            self.now_index+=1
            list = self.GetVal()
            rank = self.GetVal()
            for i in range(rank):
                list = list[self.GetVal()]
            if isinstance(list,str):
                return list.Length
            return len(list)
        elif (command == "だいちょくだい"): # ランダムアクセス
            self.now_index+=1
            list = self.GetVal()
            rank = self.GetVal()
            for i in range(rank):
                list = list[self.GetVal()]
            return list
        elif (command == "ちょくだいだいちょく"): # 論理演算
            self.now_index+=1
            s = self.commands[self.now_index]
            self.now_index+=1
            res = []
            t = 0
            for i in range(4):
                if (s[t] == 'ち'):
                    res[i] = 1
                    t += 3
                elif (s[t] == 'だ'):
                    res[i] = 0
                    t += 2
            a = self.Interpreter.BoolToInt(not self.EqualToZero(self.GetVal()))
            b = self.Interpreter.BoolToInt(not self.EqualToZero(self.GetVal()))
            return res[a * 2 + b]
        elif (command == "だいだいちょくだいちょく"): # deq pop_front
            self.now_index+=1
            deq = self.vars[self.commands[self.now_index]]
            self.now_index+=1
            return deq.PopFront()
        elif (command == "だいだいちょくちょくだい"): # deq pop_back
            self.now_index+=1
            deq = self.vars[self.commands[self.now_index]]
            self.now_index+=1
            return deq.PopBack()
        elif (command == "だいちょくだいちょくちょく"): # pq pop
            self.now_index+=1
            pq = self.vars[self.commands[self.now_index]]
            self.now_index+=1
            return pq.Pop()
        elif (command == "だいちょくちょくだいちょく"): # pq count
            self.now_index+=1
            pq = self.vars[self.commands[self.now_index]]
            self.now_index+=1
            return len(pq)
        elif (command == "だいちょくだいだいちょく"): # deq count
            self.now_index+=1
            deq = self.vars[self.commands[self.now_index]]
            self.now_index+=1
            return len(deq)
        elif (command in self.interpreter.funcs): # 関数呼び出し
            self.now_index+=1
            return self.CallFunc(command)
        else:
            ret=self.now_index
            self.now_index+=1
            return self.vars[self.commands[ret]]

    # 0と空文字列、空リストを0と見なす
    def EqualToZero(self,val):
        if isinstance(val,int):
            return val==0
        return len(val)==0 or ord(val[0])==0

    # 関数呼び出し
    def CallFunc(self,name):
        function = self.interpreter.funcs[name]
        arg_num2 = function.arg_num
        args2 = []
        for i in range(arg_num2):
            args2.append(self.GetVal())
        return function.Run(args2)

    # 変数の定義or代入
    def SetVar(self,name,val):
        # すでに宣言されていたら代入
        self.vars[name]=val

    # リストに要素を追加
    # index: 要素を追加する場所(デフォルトで末尾)
    def ListInsert(self, name, index, val):
        list = self.vars[name]
        rank = len(index)
        for i in range(rank):
            list = list[index[i]]
        id = index[rank - 1]
        if (id == -1):
            id = len(list)
        list.insert(id, val)

    # リストの要素に値を代入
    def SetListElement(self,name,index,val):
        list = self.vars[name]
        rank = len(index)
        for i in range(rank):
            list = list[index[i]]
        list = val

    # リストから要素を削除
    # indexはListInsertに同じ
    def ListDelete(self,name,index):
        list = self.vars[name]
        rank = len(index)
        for i in range(rank):
            list = list[index[i]]
        id = index[rank - 1]
        list.pop(len(list)-1 if id < 0 else id)

    def Run(self,args):
        self.vars = {}
        while_stack = Stack()
        if_stack = Stack()
        self.now_index = 3

        # 引数を変数リストに格納
        for i in range(self.arg_num):
            self.vars[self.commands[self.now_index]]=args[i]
            self.now_index+=1
        while True:
            command = self.commands[self.now_index]
            if (command == "ちょくちょくだい" and not(self.commands[self.now_index - 1] == "ちょく" or self.commands[self.now_index - 1] == "だい")):
                break
            self.now_index+=1
            if (command == "ちょくちょく"): # 変数の定義or代入
                name = self.commands[self.now_index]
                self.now_index+=1
                self.SetVar(name, self.GetVal())
            elif (command == "だいだいだいだい"): # if始まり
                begin = self.now_index - 1
                if (self.EqualToZero(self.GetVal())):
                    self.now_index = self.ifs[begin][0] + (self.ifs[begin][0] == self.ifs[begin][1])
                else:
                    if_stack.Push(begin)
            elif (command == "だいだいだいちょく"): # else if
                begin = self.now_index - 1
                if (len(if_stack) == 0 or self.ifs[if_stack.Peek()][0] != begin):
                    if (self.EqualToZero(self.GetVal())):
                        self.now_index = self.ifs[begin][0] + (self.ifs[begin][0] == self.ifs[begin][1])
                    else:
                        if_stack.Push(begin)
                else:
                    self.now_index = self.ifs[if_stack.Pop()][1] + 1
            elif (command == "だいだいちょくだい"): # if文終わり
                if_stack.Pop()
            elif (command == "だいだいちょくちょく"): # while文始まり
                begin = self.now_index - 1
                if (self.EqualToZero(self.GetVal())):
                    self.now_index = whiles[begin] + 1
                else:
                    while_stack.Push(begin)
            elif (command == "だいちょくだいだい"): # break
                self.now_index = whiles[while_stack.Pop()]
            elif (command == "だいちょくだいちょく"): # while文終わり
                self.now_index = while_stack.Pop()
            elif (command == "ちょくだいちょく"): # 数字の入力の受け取り
                name = self.commands[self.now_index]
                self.SetVar(name, int(self.interpreter.ReadStr()))
                self.now_index+=1
            elif (command == "ちょくだいだいだい"): # 文字列の入力の受け取り
                name = self.commands[self.now_index]
                self.SetVar(name, interpreter.ReadStr())
                self.now_index+=1
            elif (command == "ちょくだいだいだいだい"): # 一行丸々受け取り
                name = self.commands[self.now_index]
                self.SetVar(name, input())
                self.now_index+=1
            elif (command == "だいちょく"): # 標準出力
                print(self.GetVal())
            elif (command == "だいだいだい"):
                name = self.commands[self.now_index]
                self.now_index+=1
                rank = self.GetVal()
                list = self.vars[name]
                for i in range(rank):
                    list = list[self.GetVal()]
                id = self.GetVal()
                val = self.GetVal()
                list[id] = val
            elif (command == "だいちょくちょくちょく"): # リストへの要素の追加
                name = self.commands[self.now_index]
                self.now_index+=1
                rank = self.GetVal()
                index = []
                for i in range(rank):
                    index.append(self.GetVal())
                element = self.GetVal()
                ListInsert(name, index, element)
            elif (command == "だいちょくちょくだい"): # リストの要素の削除
                name = self.commands[self.now_index]
                self.now_index+=1
                rank = self.GetVal()
                index = []
                for i in range(rank):
                    index.append(self.GetVal())
                ListDelete(name, index)
            elif (command == "だいだいだいちょくだい"): # 昇順ソート
                name = self.commands[self.now_index]
                self.now_index+=1
                list = self.vars[name]
                list.sort()
            elif (command == "だいだいだいちょくちょく"): #降順ソート
                name = self.commands[self.now_index]
                self.now_index+=1
                list = self.vars[name]

                list.reverse()
            elif (command == "だいだいちょくだいちょく"): # deq pop_front
                deq = self.vars[self.commands[self.now_index]]
                self.now_index+=1
                deq.PopFront()
            elif (command == "だいだいちょくちょくだい"): # deq pop_back
                deq = self.vars[self.commands[self.now_index]]
                self.now_index+=1
                deq.PopBack()
            elif (command == "だいだいちょくちょくちょく"): # deq push_front
                deq = self.vars[self.commands[self.now_index]]
                self.now_index+=1
                deq.PushFront(self.GetVal())
            elif (command == "だいちょくだいだいだい"): # deq push_back
                deq = self.vars[self.commands[self.now_index]]
                self.now_index+=1
                deq.PushBack(self.GetVal())
            elif (command == "だいちょくだいちょくちょく"): # pq pop
                pq = self.vars[self.commands[self.now_index]]
                self.now_index+=1
                pq.Pop()
            elif (command == "だいちょくちょくだいだい"): # pq push
                pq = self.vars[self.commands[self.now_index]]
                self.now_index+=1
                pq.Push(self.GetVal())
            elif (command == "ちょくだいだい"): # return
                return self.GetVal()
            elif (command == "ちょくちょくだい"): # 関数の終了
                return None
            elif (command in self.interpreter.funcs): # 関数呼び出し
                self.CallFunc(command, self.now_index)
            elif (command in self.vars): # 変数参照
                self.GetVal()
            else:
                raise Exception("no function or variable named {command} found.\n current index is {now_index}.".format(command=command,now_index=self.now_index-1))
        return None


main()
