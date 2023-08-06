class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left
    
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

inverted_tree = invert_tree(root)

def print_level_order(root):
    if root is None:
        return
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print_level_order(inverted_tree)
