def parent(i):return (i-1)//2
def leftchild(i):return 2*i+1
def rightchild(i):return 2*i+2
class BST:
    def __init__(self):
        self.tree=[None]*16
    def find(self,data):
        i=0
        while(True):
            if(self.tree[i]==data or self.tree[i]==None):
                return i
            if(self.tree[i]>data):
                i=leftchild(i)
            elif(self.tree[i]<data):
                i=rightchild(i)

    def append(self,data):
        i=self.find(data)
        if(self.tree[i]==None):
            self.tree[i]=data
        elif(self.tree[i]>data):
            self.tree[leftchild(i)]=data
        else:
            self.tree[leftchild(i)]=data

T=BST()
print("HELLO")
while(True):
    i=int(input())
    if(i==1):
        l=list(map(int,input().split()))
        for i in l:
            T.append(i)
        print(T.tree)
    elif(i==2):
        print(T.find(int(input())))
    else:
        exit()
