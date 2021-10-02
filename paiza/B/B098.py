# FAILED


def main():
    num_of_posts, time_to_observe, time_to_buzz, number_to_buzz = read_stdin()
    timeline: tuple[tuple[int]] = fetch_timeline(time_to_observe)
    posts = get_all_posts(timeline, num_of_posts)

    for post in posts:
        print(did_buzz(post, time_to_buzz, number_to_buzz))


def read_stdin():
    return tuple(map(int, input().split()))


def fetch_timeline(hours: int):
    return tuple([tuple(map(int, input().split())) for _ in range(hours)])


def extract_post(tl, post_position):
    return tuple([tl[i][post_position] for i in range(tl.__len__())])


def get_all_posts(tl, num_of_posts):
    posts = []
    for i in range(num_of_posts):
        posts.append(extract_post(tl, i))
    return tuple(posts)


def did_buzz(post, time_to_observe, criterion_to_buzz):
    for i in range(post.__len__()):
        s = i - time_to_observe if i - time_to_observe >= 0 else 0

        if sum(post[s : i + 1]) >= criterion_to_buzz:
            return f"yes {i+1}"
    return "no 0"


if __name__ == "__main__":
    main()
