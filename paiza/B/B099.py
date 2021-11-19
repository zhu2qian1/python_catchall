def can_pass(x, route):
    for c in route:
        if c >= x:
            return False
    return True


map_size, unbearable_rain = tuple(map(int, input().split()))

_paths = []
for _ in range(map_size):
    _paths.append(list(map(int, input().split())))

paths = [[0] for _ in range(map_size)]
for i in range(len(_paths)):
    for j in range(map_size):
        paths[j].append(_paths[i][j])


route_numbers = []
for i in range(len(paths)):
    if can_pass(unbearable_rain, paths[i]):
        route_numbers.append(i + 1)

if not route_numbers:
    print("wait")
else:
    print(*route_numbers)
