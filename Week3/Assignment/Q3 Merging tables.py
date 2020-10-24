class disjoint_set:
    def __init__(self,n,m):
        self.parent=[None]*n
        self.rank=[None]*n
        self.max=m

    def makeset(self,i,z):
        self.parent[i]=i
        self.rank[i]=z

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
            self.rank[i_id]+=self.rank[j_id]
            if(self.max<=self.rank[i_id]):
                self.max=self.rank[i_id]
        else:
            self.parent[i_id]=j_id
            self.rank[j_id]+=self.rank[i_id]
            if(self.max<=self.rank[j_id]):
                self.max=self.rank[j_id]


n,m=map(int,input().split())
l=list(map(int,input().split()))
m1=max(l)
d=disjoint_set(n,m1)
for i in range(n):
    d.makeset(i,l[i])
ans=[]
for _ in range(m):
    p,q=map(int,input().split())
    d.merge(p-1,q-1)
    ans.append(d.max)
for i in ans:print(i)
