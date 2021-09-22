def main():
    taxis: list[tuple[int]] = list()

    num_of_taxi, distance = tuple(map(int, input().split()))

    for _ in range(num_of_taxi):
        taxis.append(list(map(int, input().split())))

    lowest_fare = float("inf")
    highest_fare = 0

    for taxi in taxis:
        if lowest_fare >= calculate_fare(distance, taxi):
            lowest_fare = calculate_fare(distance, taxi)
        if highest_fare <= calculate_fare(distance, taxi):
            highest_fare = calculate_fare(distance, taxi)

    print(lowest_fare, highest_fare)


def calculate_fare(distance: int, info: tuple) -> int:
    """calculate fare
    0 -> id, 初乗り距離
    1 -> if, 初乗り運賃
    2 -> ad, 加算距離
    3 -> af, 加算料金"""
    if distance < info[0]:
        return info[1]

    d = distance - info[0]

    n = 0

    while d >= 0:
        d -= info[2]
        n += 1

    return info[1] + info[3] * n


if __name__ == "__main__":
    main()
