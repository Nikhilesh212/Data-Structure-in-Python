import heapq
n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=[]
for i in range(n):
    if(i>=m):
        break
    print(i,0)
for i in range(n):
    if(i>=m):
        break
    l1.append([l[i],i])
print(l1)
heapq.heapify(l1)
for i in range(n,m):
    temp=heapq.heappop(l1)
    heapq.heappush(l1,[l[i]+temp[0],temp[1]])
    print(temp[1],temp[0])
