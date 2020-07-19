# ID 33625323

def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


class Solution():
    def __init__(self, name, lst, pos):
        self.name = name
        self.data = [int(x) for x in lst]
        self.res = sum(x for x in self.data if x > 0)
        self.pos = pos

    def __gt__(self, other):
        if self.is_kondratiy() and other.is_kondratiy():
            return True
        if self.is_kondratiy():
            return False
        if other.is_kondratiy():
            return True
        if self.res == other.res and self.name == other.name:
            if self.pos > other.pos:
                return False
            return True
        if self.res == other.res:
            return self.name > other.name
        return self.res < other.res

    def is_kondratiy(self):
        return set('kondratiy').issubset(set(self.name))


length = int(input())
array = []
for i in range(length):
    temp = [x for x in input().split()]
    array.append(Solution(temp[0], temp[1:], i))

heap_sort(array)

for instance in array:
    print(instance.name, *instance.data)
