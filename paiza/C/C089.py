h, w = tuple(input().split())
board = []
for _ in range(int(h)):
    for j in input():
        board.append(j)

scores = []
for _ in range(int(h)):
    for j in tuple(map(int, input().split())):
        scores.append(j)

score = 0
for i, j in zip(board, scores):
    if i == "o":
        score += j
print(score)
