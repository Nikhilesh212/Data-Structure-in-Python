import random
def hash(S, x, p):
    h = 0
    for i in S:
        h += ( ord(i))
    return h

def precomputehash(S,p,x):
    arr=[None]*(len(S))
    i=0
    while(i<len(s)):
        arr[i]=hash(s[0:i+1],x,p)
        i+=1
    return arr

s=input()
x=1000000007
p=random.randint(1,x-1)
arr=precomputehash(s,x,p)
#print(arr)
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    #print(hash(s[a:a+c],p,x),hash(s[b:b+c],p,x),arr[a+c-1]-arr[a-1])
    if(a==b or (arr[a+c-1]-arr[a-1]==arr[b+c-1]-arr[b-1] and s[a:a+c]==s[b:b+c])):
        print("Yes")
    else:
        print('No')
