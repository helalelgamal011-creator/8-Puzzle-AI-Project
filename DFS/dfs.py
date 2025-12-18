from common.puzzle_utils import get_neighbors, GOAL_STATE

def dfs(start, limit=50):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state == GOAL_STATE:
            return path
        if len(path) < limit:
            for n in get_neighbors(state):
                if n not in visited:
                    visited.add(n)
                    stack.append((n, path + [n]))
