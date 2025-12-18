import heapq
from common.puzzle_utils import get_neighbors, GOAL_STATE

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal = GOAL_STATE.index(state[i])
            distance += abs(i//3 - goal//3) + abs(i%3 - goal%3)
    return distance

def astar(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == GOAL_STATE:
            return path
        if state not in visited:
            visited.add(state)
            for n in get_neighbors(state):
                heapq.heappush(
                    pq, (g+1+heuristic(n), g+1, n, path + [n])
                )
