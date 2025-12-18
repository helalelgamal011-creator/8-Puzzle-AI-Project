GOAL_STATE = (1,2,3,4,5,6,7,8,0)

MOVES = {
    0:[1,3], 1:[0,2,4], 2:[1,5],
    3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
    6:[3,7], 7:[4,6,8], 8:[5,7]
}

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    for move in MOVES[zero]:
        new = list(state)
        new[zero], new[move] = new[move], new[zero]
        neighbors.append(tuple(new))
    return neighbors

def manhattan(state):
    dist = 0
    for i, val in enumerate(state):
        if val == 0:
            continue
        r1,c1 = divmod(i,3)
        r2,c2 = divmod(val-1,3)
        dist += abs(r1-r2)+abs(c1-c2)
    return dist

def print_puzzle(state):
    for i in range(0,9,3):
        print(state[i],state[i+1],state[i+2])
    print()
