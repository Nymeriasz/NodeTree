class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key<root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root    

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)    

root = TreeNode(20)
insert(root, 4)
insert(root, 24)
insert(root, 5)
insert(root, 2)
insert(root, 44)
insert(root, 25)

inorder_traversal(root)