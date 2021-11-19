CANNOT_DIVIDE = "No"
h, w = tuple(map(int, input().split()))


def read_chocolate_info(height, width):
    chocolate = []
    for h in range(height):
        chocolate.append(list(map(int, input().split())))
    return chocolate


chocolate = read_chocolate_info(h, w)


def divide_chocolate_row(row):
    for i in range(len(row)):
        if sum(row[:i]) == sum(row[i:]):
            return i
    return -1


def divide_whole_chocolate(chocolate):
    indices = []
    for row in chocolate:
        memo = divide_chocolate_row(row)
        if memo == -1:
            return CANNOT_DIVIDE
        indices.append(memo)
    return indices


def process_result(indices, width):
    result = []
    for i in indices:
        result.append(["A" * i + "B" * (width - i)])
    return result


result = divide_whole_chocolate(chocolate)
if CANNOT_DIVIDE in result:
    print(CANNOT_DIVIDE)
else:
    print("Yes")
    r = process_result(result, w)
    for _ in r:
        print(*_, sep="")
