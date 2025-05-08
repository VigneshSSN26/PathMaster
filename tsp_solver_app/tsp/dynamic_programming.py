def solve_tsp_dp(dist):
    from itertools import permutations
    n = len(dist)
    min_cost = float('inf')
    best_path = []
    for perm in permutations(range(n)):
        cost = sum(dist[perm[i]][perm[i+1]] for i in range(n-1)) + dist[perm[-1]][perm[0]]
        if cost < min_cost:
            min_cost = cost
            best_path = perm
    return list(best_path) + [best_path[0]], min_cost
