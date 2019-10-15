

path = list()


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    path.append(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'Arad': set(['Zerind', 'Timisoara', 'Sibiu']),
         'Zerind': set(['Oradea', 'Arad']),
         'Timisoara': set(['Arad', 'Lugoj']),
         'Lugoj': set(['Mehadia', 'Timisoara']),
         'Mehadia': set(['Lugoj', 'Drobeta']),
         'Drobeta': set(['Mehadia', 'Craiova']),
         'Craiova': set(['Drobeta', 'Pitesti', 'RimnicuVilcea']),
         'Pitesti': set(['Craiova', 'Bucharest']),
         'RimnicuVilcea': set(['Craiova', 'Pitesti', 'Sibiu']),
         'Oradea': set(['Zerind', 'Sibiu']),
         'Sibiu': set(['Fagaras', 'Oradea']),
         'Fagaras': set(['Sibiu', 'Bucharest']),
         'Bucharest': set(['Giurgiu', 'Urziceni']),
         'Giurgiu': set(['Bucharest']),
         'Urziceni': set(['Hirsova', 'Vaslui']),
         'Hirsova': set(['Urziceni', 'Eforie']),
         'Vaslui': set(['Iasi', 'Urziceni']),
         'Iasi': set(['Neamt']),
         'Neamt': set(['Iasi']),
         'Eforie': set(['Hirsova'])}

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

dfs(graph, 'Arad')

totalCost = 0
c = 0
# bIndex is index for Bucharest
bIndex = 0
while path[bIndex] != 'Bucharest':
    bIndex = bIndex + 1
# print(bIndex)
print("Path is")
for x in range(0, bIndex + 1):
    print(path[x])

for i in range(0, bIndex):
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
