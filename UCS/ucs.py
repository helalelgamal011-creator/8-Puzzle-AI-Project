import heapq
from common.puzzle_utils import get_neighbors, GOAL_STATE

def ucs(start):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, state, path = heapq.heappop(pq)
        if state == GOAL_STATE:
            return path
        if state not in visited:
            visited.add(state)
            for n in get_neighbors(state):
                heapq.heappush(pq, (cost+1, n, path + [n]))
