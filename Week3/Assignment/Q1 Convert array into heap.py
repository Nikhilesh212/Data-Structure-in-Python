def p(i):
    return (i-1)//2
def leftchild(i):
    return (2*i)+1
def rightchild(i):
    return (2*i)+2
def shiftdown(i,heap,count):
    maxidx=i
    l=leftchild(i)
    if l<len(heap) and heap[l]<heap[i]:
        maxidx=l
    r=rightchild(i)
    if r<len(heap) and heap[r]<heap[maxidx]:
        maxidx=r
    if i!=maxidx:
        heap[maxidx],heap[i]=heap[i],heap[maxidx]
        count.append((i,maxidx))
        shiftdown(maxidx,heap,count)
    return count

N=int(input())
n=list(map(int,input().split()))

i=N//2
c=[]
while(i>=0):
    shiftdown(i,n,c)
    i-=1
print(len(c))
for i in c:
    print(*i)
