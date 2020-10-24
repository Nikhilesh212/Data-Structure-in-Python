import random

class hash_table:
    def __init__(self):
        self.count=0
        self.table = [None] * 10
        self.p=100_000_000_0019
        self.a=random.randint(1,self.p-1)
        self.b=random.randint(0,self.p-1)

    def hash(self, x,size):
        x=int(x)
        return (((self.a*x + self.b) % self.p) % size)

    def rehash(self):
        if(self.count/len(self.table) > 0.1):
            size=len(self.table)
            tablenew = [None]*(2*size)
            self.a=random.randint(1,self.p-1)
            self.b=random.randint(0,self.p-1)
            for i in self.table:
                if i:
                    tablenew[self.hash(i[0],size)]=i
            self.table=tablenew

    def __setitem__(self, key, data):
        self.rehash()
        size=len(self.table)
        self.table[self.hash(key,size)]=[key,data]
        self.count+=1

    def __getitem__(self,key):
        return self.table[self.hash(key,len(self.table))][1]

h=hash_table()
h['9689611453']='Nikhilesh'
h['7020180971']='Jio'
print(h['9689611453'])
