n = int(input())
d = list(map(int, input().split()))


def has_two_holidays(d):
    if sum(d) <= 5:
        return True
    return False


def find_longest_workdays_with_two_holidays(d):
    s, e = None, None
    for i in range(len(d) - 7):
        if has_two_holidays(d[i : i + 7]):
            if s == None:
                s = i
            else:
                e = i + 7
    print(e - s + 1 if s != None else 0)


find_longest_workdays_with_two_holidays(d)
