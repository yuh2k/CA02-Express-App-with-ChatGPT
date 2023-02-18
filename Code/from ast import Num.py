class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def func(node):
    res = -1
    if not node:
        return 0
    def dfs(node, min_val, max_val):
        nonlocal res
        if not node:
            return
        max_val = max(max_val, node.val)
        min_val = min(min_val, node.val)
        res = max(res, max_val - min_val)
        dfs(node.left, min_val, max_val)
        dfs(node.right, min_val, max_val)
    dfs(node, node.val, node.val)
    return res

tree1 = Node(8, Node(1), Node(2))
tree2 = Node(8, Node(8, Node(8, Node(8))), Node(8))
print(func(None))
#     8
#   8   8
#  8
# 8
# Time: O(n)
# Space: O(n)




# 1. analyze complexity
# 2. write tcs
