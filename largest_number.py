# ID 33568007


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


def largest_number(nums):

    if len(nums) == 0:
        return ""

    result = sorted(nums, key=LargerNumKey)

    if result[0] == 0:
        return '0'
    return ''.join(result)


length = input()
arr = input().split()
print(largest_number(arr))
