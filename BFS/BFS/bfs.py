from collections import deque
from common.puzzle_utils import get_neighbors, GOAL_STATE

def bfs(start):
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == GOAL_STATE:
            return path
        for n in get_neighbors(state):
            if n not in visited:
                visited.add(n)
                queue.append((n, path + [n]))
