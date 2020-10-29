from sys import stdin as s
from random import randint as r

class HashTable:
    def __init__(self,m):
        self.m = m
        self.arr = [None] * self.m
        self.p=1000000007
        self.n = 0
        self.a = r(1, self.p - 1)
        self.b = r(0, self.p - 1)

    def hash(self, x):
        temp=0
        a=0
        size=len(self.arr)
        for i in x:
            temp+=ord(i)*(263**a)
            a+=1
        return (((temp) % self.p) % size)

    # def rehash(self):
    #     lf = (self.n / self.m)
    #     if lf < 0.9:
    #         return
    #     self.m *= 2
    #     arrnew = [None] * self.m
    #     for i in range(self.m // 2):
    #         k = self.arr[i]
    #         if k:
    #             key = hash(k)
    #             arrnew[key] = k

    def remove(self, key):
        h = self.hash(key)
        if self.arr[h]:
            for i in range(len(self.arr[h])):
                if self.arr[h][i][0] == key:
                    del self.arr[h][i]
                    return

    def __getitem__(self, key):

        h = self.hash(key)
        if not self.arr[h]:
            return 'not found'
        for i in self.arr[h]:
            if i[0] == key:
                return i[1]
        return 'not found'

    def setitem(self, key):
        # self.rehash()
        # self.n += 1
        data =key
        h = self.hash(key)
        if self.arr[h]:
            self.arr[h].append([data])
        else:
            self.arr[h] = [[data]]

    def __repr__(self):
        return "HashTable({})".format(self.arr)

n=int(input())
h=HashTable(n)
for _ in range(int(input())) :
    s=input()
    l=[]
    l=s.split(' ')
    if(l[0]=='add'):
        h.setitem(l[1])
    elif(l[0]=='find'):
        temp=h[l[1]]
        if(temp!='not found'):
            print("yes")
        else:
            print('no')
    elif(l[0]=='check'):
        print(h.arr[int(l[1])])
    else:
        h.remove(l[1])
