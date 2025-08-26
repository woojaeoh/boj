import sys

input = sys.stdin.readline
N = int(input())
tree = {}
nodes ,child = set(),set()

for _ in range(N):
    a, l, r = input().split()
    tree[a] = (l , r)
    nodes.add(a)
    if l != ".":
        child.add(l)
    if r != ".":
        child.add(r)
            
root = (nodes-child).pop()

def preorder(node):
    if node == '.':
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])
    
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])
    
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")
    
preorder(root)
print()
inorder(root)
print()
postorder(root)
