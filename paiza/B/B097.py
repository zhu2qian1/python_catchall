debug = False


def main():
    _ = int(input())
    seat_info = [0] * _

    _ = int(input())
    groups = []

    elapsed_minutes = 0

    for __ in range(_):
        groups.append(tuple(map(int, input().split())))

    # popで回せるようにに反転する
    groups.reverse()

    # グループの情報を取得する
    group = groups.pop()

    # 最初のグループを着座させる
    for _ in range(group[0]):
        seat_group(group, seat_info, 0)

    while 1:
        try:
            group = groups.pop()
            if debug:
                print("next group:", group)

            while 1:
                # グループが着座可能かチェックする
                stat = can_seat_group(group, seat_info)
                if debug:
                    print("deeper loop:", seat_info, *stat)
                if stat[0]:

                    # 着座可能であれば着座させてbreak
                    n = stat[1]
                    seat_group(group, seat_info, n)
                    if debug:
                        print("seated stat:", seat_info)
                    break

                # そうでなければ一分経過させて経過時間をインクリメント
                else:
                    elapse_one_minute(seat_info)
                    elapsed_minutes += 1
                    if debug:
                        print("time elapsed:", elapsed_minutes)

        except IndexError:
            elapsed_minutes += max(seat_info)
            break

    print(elapsed_minutes)


def can_seat_group(group, seat_info):
    size = group[0]
    index = []  # インデクス情報をしまうための箱
    vacant_seats = 0  # カウンター的な
    for i, seat in enumerate(seat_info):
        if seat == 0:
            index.append(i)
            # もし空いていたらvacant_seatsをインクリメント
            vacant_seats += 1
            if vacant_seats == size:
                # もしvacant_seatsがsizeと一緒（グループが座れる余裕がある）ならTrue
                return True, index[0]
        else:
            # 空席がなかったらカウンターとインデクス情報をリセット
            vacant_seats = 0
            index = []
    return False, []


def seat_group(group, seat_info, start):
    for i, j in zip(range(start, group[0] + start), group[1:]):
        seat_info[i] = j


def elapse_one_minute(seat_info):
    for i in range(len(seat_info)):
        if seat_info[i] == 0:
            continue
        seat_info[i] -= 1


if __name__ == "__main__":
    main()
