def read_initial_conditions():
    return tuple(map(int, input().split()))


def read_integers():
    return list(map(int, input().split()))


def read_queries(num):
    return [tuple(map(int, input().split())) for _ in range(num)]


def calc_average_of_bulbs_between(bulbs_on_tree, query):
    sum_of_bulbs = 0
    return sum(bulbs_on_tree[query[0] - 1 : query[1]]) // (query[1] - query[0] + 1)


def add_bulbs_on_tree(bulbs_on_tree, query, number_of_additional_bulbs):
    for i in range(query[0] - 1, query[1]):
        bulbs_on_tree[i] += number_of_additional_bulbs


def process_query(bulbs_on_tree, query, safety_criterion):
    if (a := calc_average_of_bulbs_between(bulbs_on_tree, query)) < safety_criterion:
        add_bulbs_on_tree(bulbs_on_tree, query, safety_criterion - a)


def main():
    number_of_trees, safety_criterion = read_initial_conditions()
    bulbs_on_tree = read_integers()
    number_of_queries = int(input())
    queries = read_queries(number_of_queries)
    for query in queries:
        process_query(bulbs_on_tree, query, safety_criterion)
    print(*bulbs_on_tree)


if __name__ == "__main__":
    main()
