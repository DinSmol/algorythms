# ID 33551377

def binary_search(alist, first, last, item):
    midpoint = (first + last)//2

    if last >= first:
        if alist[midpoint] == item:
            return midpoint

        if alist[first] <= alist[midpoint]:
            if alist[first] <= item and item < alist[midpoint]:
                return binary_search(alist, first, midpoint-1, item)
            else:
                return binary_search(alist, midpoint+1, last, item)

        else:
            if alist[midpoint] < item and item <= alist[last]:
                return binary_search(alist, midpoint + 1, last, item)
            else:
                return binary_search(alist, first, midpoint - 1, item)

    else:
        return -1


def find_index():
    length = int(input())

    if length == 0:
        print(-1)
        return
    else:
        item = int(input())
        arr = [int(x) for x in input().split()]
        print(binary_search(arr, 0, length - 1, item))


find_index()
