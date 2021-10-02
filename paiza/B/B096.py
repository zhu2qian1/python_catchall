# SUCCESS!


def main():
    height, width = read_size()
    field = read_field(height)

    print(explode_bombs(field).__len__())


def read_size():
    return tuple(map(int, input().split()))


def read_row_field():
    row = input()
    bomb_map = []
    for c in row:
        bomb_map.append(1 if c == "#" else 0)
    return bomb_map


def read_field(height):
    field = []

    for _ in range(height):
        field.append(read_row_field())

    return field


def explode_bombs(field):
    coordinates = set()
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell == 1:
                for i in range(len(row)):
                    coordinates.add((y, i))
                for i in range(len(field)):
                    coordinates.add((i, x))
    return coordinates


if __name__ == "__main__":
    main()
