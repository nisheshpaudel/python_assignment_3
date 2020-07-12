def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def quickSort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            quickSort(items, low, split_index)
            quickSort(items, split_index + 1, high)

    quickSort(nums, 0, len(nums) - 1)


data_list = [22, 16, 43, 27, 33, 41, 17, 21, 56]
quick_sort(data_list)
print(data_list)