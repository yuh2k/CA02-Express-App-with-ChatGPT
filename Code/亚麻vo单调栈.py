# bq： challenge problem + make decision without help。 
# code： 给数组 如 4，5，2，25。如果后面有当前位大的，就取后面第一位大的元素，没有的话，就取-1，输出结果为string 52525-1

# arr = [4,5,2,25]
#          ↑


stack = [5]
def f(nums) -> str:
    stack = []
    res = [-1] * len(nums)

    for i, t in enumerate(nums):
        while stack and t > nums[stack[-1]]:
            ind = stack.pop()
            res[ind] = nums[i]
    
        stack.append(i)

    return ''.join(list(map(str, res)))

# print(f(nums))




# def f(nums) -> str:
#     # brute force
#     n = len(nums)
#     res = ''
#     for i in range(n):
#         a = nums[i]
#         temp = False
#         for j in range(i + 1, n):
#             b = nums[j]
#             if b > a:
#                 temp = True
#                 res += str(b)
#                 break
#         if not temp:
#             res += '-1'
    
#     return res


    


            





if __name__ == '__main__':
    nums = [4,5,2,25]
    print(f(nums))