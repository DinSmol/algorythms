# ID 33568069


def radix_sort(array):

    length = len(str(max(array)))
    range_ = 10

    for i in range(length):
        temp = [[] for k in range(range_)]

        for item in array:
            figure = item // 10**i % 10
            temp[figure].append(item)
        array = []

        for k in range(range_):
            array = array + temp[k]
    print(*array)


length = input()
array = [int(x) for x in input().split()]
radix_sort(array)
