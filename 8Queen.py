import random

N = 8

def is_valid(board, row, col):
    for r in range(row):
        c = board[r]
        # same column OR diagonal conflict
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve(row, board, solutions):
    if row == N:
        solutions.append(board.copy())
        return
    
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve(row + 1, board, solutions)
            board[row] = -1  # backtrack


def calculate_weight(solution, weights):
    return sum(weights[(row, col)] for row, col in enumerate(solution))


# ---------- Generate all solutions ----------
board = [-1] * N
solutions = []
solve(0, board, solutions)

# ---------- Assign random weights ----------
weights = {}
for r in range(N):
    for c in range(N):
        weights[(r, c)] = random.randint(1, 99)

print("Numbers (weights):")
for k, v in weights.items():
    print(k, v)

print("\n------------------")
print("Ways to place queens and their weight:")

final_list = []
max_weight = 0

for sol in solutions:
    w = calculate_weight(sol, weights)
    final_list.append((sol, w))
    print(sol, w)
    if w > max_weight:
        max_weight = w

print("\n------------------")
print("Final Solution(s):")

for sol, w in final_list:
    if w == max_weight:
        print(sol, w)

input()
