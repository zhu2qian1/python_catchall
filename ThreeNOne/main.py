def three_to_one(arg: int) -> int:
    if arg == 1:
        return 0
    if arg % 2 == 0:
        print(arg)
        return three_to_one(arg // 2)
    else:
        print(arg)
        return three_to_one(arg * 3 + 1)
