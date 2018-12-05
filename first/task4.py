a = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]


def remove_duplicates(args):
    result = sorted(args)
    i = len(result)-1
    while i > 0:
        if result[i] == result[i-1]:
            del result[i]
        i -= 1
    print(result)


def find_3max(args):
    result = sorted(args)
    print(result[-3:])


def find_min_index(args):
    print(args.index(min(args)))


def reverse_order(args):
    print(args[::-1])


remove_duplicates(a)
find_3max(a)
find_min_index(a)
reverse_order(a)
