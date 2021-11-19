# transpose a 2d array
def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


def read_integers():
    return list(map(int, input().split()))
