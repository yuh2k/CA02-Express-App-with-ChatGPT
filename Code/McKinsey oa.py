
'''
1. Reach the end in Time
'''
# def func(rows, grid, maxTime):
#     q = [(0, 0, 0)]
#     m, n = rows, len(grid[rows - 1])
#     visited = set((0, 0))
#     res = float('inf')
#     while q:
#         x, y, time = q.pop(0)
#         if (x, y) == (m - 1, n - 1):
#             res = min(res, time)
#         for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[x][y] != "#":
#                 visited.add((nx, ny))
#                 q.append((nx, ny, time + 1))
#     return res <= maxTime
    

# a = func(3, ['..##', '#.##', '#...'], 5)
# print(a)


def tasks(n, a, b):
    import collections
    prerequisites = []  
    for i in range(len(a)):
        prerequisites.append([a[i] - 1, b[i] - 1])
    edges = collections.defaultdict(list)
    visited = [0] * n
    result = list()
    valid = True
    for info in prerequisites:
        edges[info[1]].append(info[0])
    def dfs(u):
        nonlocal valid
        visited[u] = 1
        for v in edges[u]:
            if visited[v] == 0:
                dfs(v)
            elif visited[v] == 1:
                return
        visited[u] = 2
        result.append(u)
    for i in range(n):
        if valid and not visited[i]:
            dfs(i)

    return len(result)


print(tasks(6,[1,2,3,4,6,5],[7,6,4,1,2,1]))
print(tasks(2,[1],[2]))