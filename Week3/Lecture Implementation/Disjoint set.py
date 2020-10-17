class disjoint_set:
    def __init__(self):
        self.parent=[None]*10
        self.rank=[None]*10

    def makeset(self,i):
        self.parent[i]=i
        self.rank[i]=0

    def find(self,i):
        while(i!=self.parent[i]):
            i=self.parent[i]
        return i

    def merge(self,i,j):
        i_id=self.find(i)
        j_id=self.find(j)
        if(i_id==j_id):
            return
        elif(self.rank[i_id]>self.rank[j_id]):
            self.parent[j_id]=i_id
        else:
            self.parent[i_id]=j_id
            if(self.rank[i_id]==self.rank[j_id]):
                self.rank[j_id]+=1

    def common(self,i,j):
        if(self.find(i)==self.find(j)):
            return True
        else:
            return False

i=0
d=disjoint_set()
while(i!=-1):
    i=int(input())
    if(i==1):
        l=list(map(int,input().split()))
        for i in l:
            d.makeset(i)
    elif(i==2):
        j,k=map(int,input().split())
        d.merge(j,k)
    elif(i==3):
        j,k=map(int,input().split())
        print(d.common(j,k))
    print(d.parent)
