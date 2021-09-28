# 入力処理
number_of_people, length_of_song = tuple(map(int, input().split()))

sample_song_freq = [int(input()) for _ in range(length_of_song)]
singers = [
    [int(input()) for _ in range(length_of_song)] for __ in range(number_of_people)
]

# 点数計算
def calc_score(song, singer):
    score = 100
    for i in range(len(song)):
        diff = abs(song[i] - singer[i])
        if diff <= 5:
            continue
        elif diff <= 10:
            score -= 1
        elif diff <= 20:
            score -= 2
        elif diff <= 30:
            score -= 3
        else:
            score -= 5
    if score < 0:
        return 0
    else:
        return score


results = [calc_score(sample_song_freq, s) for s in singers]
print(max(results))
