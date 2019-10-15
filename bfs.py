 
import collections

parent = dict()


def bfs(graph, root):
    visited, queue = list(), collections.deque([root])
    visited.append(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                parent[vertex] = neighbour
    return visited


graph = {'Arad': list(['Zerind', 'Timisoara', 'Sibiu']),
         'Zerind': list(['Oradea', 'Arad']),
         'Timisoara': list(['Arad', 'Lugoj']),
         'Lugoj': list(['Mehadia', 'Timisoara']),
         'Mehadia': list(['Lugoj', 'Drobeta']),
         'Drobeta': list(['Mehadia', 'Craiova']),
         'Craiova': list(['Drobeta', 'Pitesti', 'RimnicuVilcea']),
         'Pitesti': list(['Craiova', 'Bucharest']),
         'RimnicuVilcea': list(['Craiova', 'Pitesti', 'Sibiu']),
         'Oradea': list(['Zerind', 'Sibiu']),
         'Sibiu': list(['Fagaras', 'Oradea']),
         'Fagaras': list(['Sibiu', 'Bucharest']),
         'Bucharest': list(['Giurgiu', 'Urziceni']),
         'Giurgiu': list(['Bucharest']),
         'Urziceni': list(['Hirsova', 'Vaslui']),
         'Hirsova': list(['Urziceni', 'Eforie']),
         'Vaslui': list(['Iasi', 'Urziceni']),
         'Iasi': list(['Neamt']),
         'Neamt': list(['Iasi']),
         'Eforie': list(['Hirsova'])}

cost = [[0, 71, 0, 151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [71, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 75, 0, 140, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [151, 0, 140, 0, 0, 0, 0, 0, 0, 0, 80, 99, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 118, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 111, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 70, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 75, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 120, 0, 138, 146, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 138, 0, 97, 0, 101, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 80, 0, 0, 0, 0, 146, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0, 211, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 0, 211, 0, 90, 85, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 85, 0, 0, 0, 98, 142, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 98, 86, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 142, 0, 0, 0, 92, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 92, 0, 87],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0]]

cityTranslation = {
    'Oradea': 0,
    'Zerind': 1,
    'Arad': 2,
    'Sibiu': 3,
    'Timisoara': 4,
    'Lugoj': 5,
    'Mehadia': 6,
    'Drobeta': 7,
    'Craiova': 8,
    'Pitesti': 9,
    'RimnicuVilcea': 10,
    'Fagaras': 11,
    'Bucharest': 12,
    'Giurgiu': 13,
    'Urziceni': 14,
    'Eforie': 15,
    'Hirsova': 16,
    'Vaslui': 17,
    'Iasi': 18,
    'Neamt': 19}

# In the Function findPath:
# b is our goal: in Ques's case Bucharest
# z is the list that stores path


def findPath(parent, b, z, root):
    if b == root:
        return
    for x in parent:
        if parent[x] == b:
            break
    y = x
    # stores parent
    z.append(y)
    # print(z)
    findPath(parent, y, z, root)


z = list()
root = 'Arad'
myQueue = []
myQueue = bfs(graph, root)
# print(myQueue)
path = list()
goal = 'Bucharest'
path.append(goal)
findPath(parent, goal, path, root)
print("Path is")
print(path)
# print(len(path))

totalCost = 0
for i in range(0, len(path) - 1):
    x = i
    c = 0
    # print("i is", i)
    # print(path[x])
    var1 = cityTranslation[path[x]]
    var2 = cityTranslation[path[x + 1]]
    var3 = cost[var1][var2]
    # print(var3)
    # print(path[i])
    # path[i] returns city name

    # cityTranslation[path[i]] returns city index
    # cost[cityTranslation[path[i]][cityTranslation[path[i+1]] returns cost with neighbour
    if var3 != 0:
        totalCost += var3
    elif var3 == 0:
        while cost[cityTranslation[path[x]]][cityTranslation[path[i + 1]]] == 0 and c < 20:
            x = x - 1
            c = c + 1
        x1 = cityTranslation[path[x]]
        x2 = cityTranslation[path[i + 1]]
        totalCost += cost[x1][x2]

print("Total cost is", totalCost)
