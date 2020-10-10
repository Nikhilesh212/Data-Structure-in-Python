class tree_node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
    def append(self,data):
        if(self.data is None):
            self.data=data
            self.right=None
            self.left=None
        else:
            temp=tree_node(data)
            curr=self
            while(True):
                if(data>=curr.data):
                    if(curr.right is None):
                        curr.right=temp
                        break
                    else:
                        curr=curr.right
                else:
                    if(curr.left is None):
                        curr.left=temp
                        break
                    else:
                        curr=curr.left
def print_tree(Tree):
    if(Tree.left):
        print_tree(Tree.left)
    if(Tree.right):
        print_tree(Tree.right)
    print(Tree.data)
def tree_height(tree):
    if(tree is None):
        return 0
    return 1+max(tree_height(tree.left),tree_height(tree.right))
n=int(input())
str=list(map(int,input().split()))
str.sort()
set(str)
Tree=tree_node()
for i in str:
    Tree.append(i)
print(len(str))
