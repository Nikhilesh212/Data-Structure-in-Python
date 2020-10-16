def p(i):
    return i//2
def leftchild(i):
    return 2*i
def rightchild(i):
    return 2*i+1

class heap:
    def __init__(self):
        self.heap=[]

    def shiftup(self,i):
        while i>=1 and self.heap[p(i)]<self.heap[i]:
            self.heap[p(i)],self.heap[i]=self.heap[i],self.heap[p(i)]
            i=p(i)

    def app(self,data):
        self.heap.append(data)
        self.shiftup(len(self.heap)-1)

    def shiftdown(self,i):
        maxidx=i
        l=leftchild(i)
        if l<len(self.heap) and self.heap[l]>self.heap[i]:
            maxidx=l
        r=rightchild(i)
        if r<len(self.heap) and self.heap[r]>self.heap[maxidx]:
            maxidx=r
        if i!=maxidx:
            self.heap[maxidx],self.heap[i]=self.heap[i],self.heap[maxidx]
            self.shiftdown(maxidx)

    def extract_max(self):
        result=self.heap[0]
        self.heap[0]=self.heap[len(self.heap)-1]
        self.heap.pop()
        self.shiftdown(0)
        return result

h=heap()
i=0
while(i!=-1):
    i=int(input())
    if(i==1):
        s=list(map(int,input().split()))
        for i in s:
            h.app(i)
    elif(i==2):
        print(h.extract_max())
    elif(i==3):
        print(*h.heap)