import heapq

romania_map = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)],
}

def bfs(start, goal):
    visited = set()
    queue = [[(start, 0)]]

    while queue:
        path = queue.pop(0)
        city = path[-1][0]

        if city == goal:
            total_cost = sum(step[1] for step in path[1:])
            return [step[0] for step in path], total_cost

        if city not in visited:
            for neighbor, cost in romania_map.get(city, []):
                new_path = list(path)
                new_path.append((neighbor, cost))
                queue.append(new_path)
            visited.add(city)
    return None, float('inf')

def dfs(start, goal, visited=None, path=None, cost=0):
    if visited is None:
        visited = set()
    if path is None:
        path = [(start, 0)]

    if start == goal:
        return path, cost

    visited.add(start)

    for neighbor, step_cost in romania_map.get(start, []):
        if neighbor not in visited:
            new_path, total_cost = dfs(neighbor, goal, visited.copy(), path + [(neighbor, step_cost)], cost + step_cost)
            if new_path:
                return new_path, total_cost

    return None, float('inf')

def ucs(start, goal):
    visited = set()
    queue = [(0, [start])]

    while queue:
        cost, path = heapq.heappop(queue)
        city = path[-1]

        if city == goal:
            return path, cost

        if city not in visited:
            visited.add(city)
            for neighbor, step_cost in romania_map.get(city, []):
                heapq.heappush(queue, (cost + step_cost, path + [neighbor]))

    return None, float('inf')
