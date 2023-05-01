class Node:
    def __init__(self,element) -> None:
        self.element = element
        self.left = None
        self.right = None


# class Tree:
#     def __init__(self,arr) -> None:
#         self.root = Node(arr[1])
# def addNode(root,i):
#     if i < root.element and root.left == None:
#         n = Node(i)
#         root.left = n
#     elif i>root.element and root.left == None:
#         n = Node(i)
#         root.right = n
#     if i < root.element and root.left != None:
#         addNode(root.left,i)
#     elif i > root.element and root.right != None:
#         addNode(root.right,i)
# def addNode(arr,n,i):
#     root = None
#     if i < n:
#         root = Node(arr[i])
#         root.left = addNode(arr,n,i*2)
#         root.right = addNode(arr,n,i*2+1)
#     return root
    
    
# def addNode(arr,n,i):
#     root = None
#     if i<n:
#         root = Node(arr[i])
#         root.left = addNode(arr,n,i*2)
#         root.right = addNode(arr,n,i*2+1)
#     return root


def addNode(root,i):
    if i<root.element and root.left == None:
        root.left = Node(i)
    elif i<root.element and root.right == None:
        root.right = Node(i)
    if i < root.element and root.left != None:
        addNode(root.left,i)
    
    elif i < root.element and root.right != None:
        addNode(root.right,i)



def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.element,end = "-->")
        inOrder(root.right)

arr = [10,20,30,40,50,60,70,80,90,100,110]



# root = addNode(arr,len(arr),1)
root = Node(arr[0])


for x in range(1,len(arr),1):
    addNode(root,arr[x])





inOrder(root)