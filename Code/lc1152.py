q = [5,2,13,3,8]

def f():
    # convert 
    q = []
    while l:
        q.append(l.val)
        l = l.next

    stack = []
    for i, num in enumerate(q):
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    # return stack
    res = ListNode(-1)
    temp = res
    for x in q:
        res.next = ListNode(x)
        res = res.next
    return temp.next

print(f(q))






# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         # self.neighbors = neighbors if neighbors else []
#         if neighbors:
#             self.neighbors = neighbors
#         else:
#             self.neighbors = []


# def display(l):
#     res = []
#     while l:
#         res.append(l.val)
#         l = l.next
#     return res

# class 傻逼:
#     def __init__(self, 值=0, 前面的=None, 后面的=None):  #constructor
#         self.值 = 值
#         self.后面的 = next

# a = 傻逼(-1)
# b = 傻逼(1)
# a.next = b
# print(display(a))

# for i in range(m):
#     for j in range(n)
# area

# recursion:函数调用自身的过程








# primitive data type:  
# reference data type: 傻逼, Array, BinaryTree


