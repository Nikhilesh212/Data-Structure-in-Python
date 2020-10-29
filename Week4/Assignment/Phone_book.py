import sys
from random import randint as r

class HashTable:
    def __init__(self):
        self.m = 1000000
        self.arr = [None] * self.m
        self.p = 1000003
        self.n = 0
        self.a = r(1, self.p - 1)
        self.b = r(0, self.p - 1)

    def hash(self, data):
        return int(((self.a * data + self.b) % self.p) % self.m)

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

    def __setitem__(self, key, data):
        h = self.hash(key)
        if self.arr[h]:
            for i in range(len(self.arr[h])):
                if self.arr[h][i][0] == key:
                    self.arr[h][i][1] = data
                    return
            self.arr[h].append([key, data])
        else:
            self.arr[h] = [[key, data]]

    def __repr__(self):
        return "HashTable({})".format(self.arr)


H = HashTable()
n = int(sys.stdin.readline())
Ans = []
for _ in range(n):
    q = list(sys.stdin.readline().split())
    q[1] = int(q[1])
    if q[0] == 'add':
        H[q[1]] = q[2]

    elif q[0] == 'find':
        Ans.append(H[q[1]])

    elif q[0] == 'del':
        H.remove(q[1])

print(*Ans, sep='\n')
print(sys.getsizeof(H.arr))
