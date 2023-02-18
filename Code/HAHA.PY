class Gaussian_Integer:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def add(self, other):
        return Gaussian_Integer(self.real + other.real, self.imag + other.imag)
    
    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Gaussian_Integer(real, imag)
    
    def __str__(self):
        return '{}+{}i'.format(self.real, self.imag)

u = Gaussian_Integer(1,1)
v = Gaussian_Integer(1,2)
w = u.multiply(u)
x = u.add(v).add(w)
print('u=',u)
print('v=',v)
print('w=',w)
print('x=',x)


# class bank:
#     def __init__(self) -> None:
#         self.money = 0
    
#     def deposit(self, amount):
#         self.money += amount
    
#     def withdraw(self, amount):
#         self.money -= amount
    
#     def check(self):
#         return self.money

# b = bank()
# b.deposit(11)
# b.withdraw(1)
# b.deposit(100)
# print(b.check())
# import openai

# # Set up the OpenAI API client
# openai.api_key = "YOUR_API_KEY"

# # test for an API key
# if openai.api_key=="YOUR_API_KEY":
#     print("You need to get an openapi api key to use this demo")
#     exit()

# # Set up the model and prompt
# model_engine = "text-davinci-003"
# prompt = input("Enter a prompt: ") # "Hello, how are you today?"

# # Generate a response
# completion = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# response = completion.choices[0].text
# print(response)

# n = 120
# divisors = [x for x in range(1, n + 1) if n % x == 0]
# print(divisors)

# def countMoveToBack(input): # input array
#     # sort given array
#     sorted_array = sorted(input)
#     sorted_idx = 0
#     for i in range(len(input)):
#         if input[i] == sorted_array[sorted_idx]:
#             sorted_idx += 1
#     min_moves = len(input) - sorted_idx
#     return min_moves

# # print(countMoveToBack([3,2,1]))

# def knapSack(W, wt, val, n):
 
#     # Base Case
#     if n == 0 or W == 0:
#         return 0
 
#     # If weight of the nth item is
#     # more than Knapsack of capacity W,
#     # then this item cannot be included
#     # in the optimal solution
#     if (wt[n-1] > W):
#         return knapSack(W, wt, val, n-1)
 
#     # return the maximum of two cases:
#     # (1) nth item included
#     # (2) not included
#     else:
#         return max(
#             val[n-1] + knapSack(
#                 W-wt[n-1], wt, val, n-1),
#             knapSack(W, wt, val, n-1))

# print(knapSack)
# # s = "321"

# # print(sorted(s))

# # time complextiy ！

# # from collections import Counter
# # arr = [1,2,3,4,5,6,1,2,3,5]

# # d = Counter(arr)
# # print(d)
# # {1: 2, 2: 2, 3: 2, 5: 2, 4: 1, 6: 1}

# # print(freq)







# # d = defaultdict(int)

# # for num in arr:
# #     if num not in d:
# #         d[num] = 1
# #     else:
# #         d[num] += 1

# # print(d.items())
# # for key, val in d.items():
# #     print(key, val)
# # print(d)






# # d = {}


# # print(d)


















# # def minimumSteps(loggedMoves):
# #     res = 0
# #     for move in loggedMoves:
# #         if move == "../":
# #             res -= 1
# #         elif move == "./":
# #             continue
# #         else:
# #             res += 1
# #     return res

# # tc1 = minimumSteps(['x/', '../', 'y/', 'z/'])
# # tc2 = minimumSteps(['o/', 'w/', 'e/', './', './', './'])

# # print(tc1, tc2)





# # def DNA_checker(s):
# #     return set(s) <= {"A","T","C","G"}

# # print(DNA_checker("ACCCCG"))

# # def func(a, b):
# #     set_a, set_b = set(a), set(b)
# #     print(set_a, set_b)
# #     return set_a <= set_b

# # print(func([1,4], [1,2,3]))
# # print(func([1,2,3], [1,2,3]))
# # print(func([1,2,3,4], [1,2,3]))
# # print(func([], [1,2,3]))




# # def func(s) -> int:

# #     from collections import Counter
# #     size = len(set(s))
# #     record = []
# #     for i, char in enumerate(s):
# #         sub = s[:i + 1]
# #         a = Counter(sub)
# #         maxi = max(dict(a).values())
# #         temp = []
# #         for k, v in dict(a).items():
# #             if v == maxi:
# #                 temp.append(k)
# #         record.append(temp)

# #     temp1 = list(map(''.join, record))
# #     temp2 = ''.join(temp1)
# #     dic2 = Counter(temp2)
# #     return max(dict(dic2).values())




# # if __name__ == '__main__':
# #     s1 = 'bccaaacb'  
# #     print(func(s1))
# #     s2 = 'adbcbcbcc'
# #     print(func(s2))
# #     s3 = 'zzzz'
# #     print(func(s3))