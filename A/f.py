def binary_search(num_list, num):
    first = 0
    last = len(num_list) - 1
    result = False
    while (first <= last and not result):
        mid = (first + last) // 2
        if num_list[mid] == num:
            result = True
        else:
            if num < num_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return result


print(binary_search([1, 2, 3, 4, 7, 9, 12], 7))
print(binary_search([1, 2, 3, 4, 7, 9, 12], 10))