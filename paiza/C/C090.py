number_distance = {
    "0": 12,
    "1": 3,
    "2": 4,
    "3": 5,
    "4": 6,
    "5": 7,
    "6": 8,
    "7": 9,
    "8": 10,
    "9": 11,
}
distance_sum = 0
for i in input():
    if i == "-":
        pass
    else:
        distance_sum += number_distance[i]
print(distance_sum * 2)
