# ID 33543538

def del_zeros(arr):
    if 0 in arr:
        return arr.index(0)
    return -1


def fotocopy():
    cnt = int(input())

    if cnt <= 1:    # one datacenter, can't to save any copy
        print('0')
        return

    arr = sorted([int(x) for x in input().split() if x != '0'])
    res = 0

    while len(arr) > 1:
        ind = del_zeros(arr)    # get and remove, if datacenter is full
        if ind >= 0:
            arr.pop(0)
            continue

        arr[0] -= 1
        arr[-1] -= 1
        res += 1
        arr = sorted(arr)

    print(res)


fotocopy()
