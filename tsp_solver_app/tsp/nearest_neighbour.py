def solve_tsp_nn(dist):
    n = len(dist)
    visited = [False] * n
    path = [0]
    visited[0] = True
    total_cost = 0
    for _ in range(n-1):
        last = path[-1]
        next_city = min((dist[last][i], i) for i in range(n) if not visited[i])[1]
        path.append(next_city)
        visited[next_city] = True
        total_cost += dist[last][next_city]
    total_cost += dist[path[-1]][path[0]]
    return path + [path[0]], total_cost
