
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insertInBst(root,node):
    if root==None:
        root=node

    else:
        if root.data<node.data:
            if root.right==None:
                root.right=node

            else:
                insertInBst(root.right,node)

        else:
            if root.left==None:
                root.left=node

            else:
                insertInBst(root.left,node)

def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

def preorder(root):
    if root!=None:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root!=None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=' ')

root=node(50)
insertInBst(root,node(30))
insertInBst(root,node(20))
insertInBst(root,node(40))
insertInBst(root,node(70))
insertInBst(root,node(60))
insertInBst(root,node(80))
print('inorder of bst= ')
inorder(root)
print()
print('preorder of bst= ')
preorder(root)
print()
print('postorder of bst= ')
postorder(root)
