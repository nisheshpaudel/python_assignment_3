def mergeSort(nums):
    if len(nums)>1:
        mid = len(nums) // 2
        left_list = nums[:mid]
        right_list = nums[mid:]

        mergeSort(left_list)
        mergeSort(right_list)
        i=j=k=0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                nums[k]=left_list[i]
                i=i+1
            else:
                nums[k]=right_list[j]
                j=j+1
            k=k+1

        while i < len(left_list):
            nums[k]=left_list[i]
            i=i+1
            k=k+1

        while j < len(right_list):
            nums[k]=right_list[j]
            j=j+1
            k=k+1

nums = [14, 6, 23, 87, 57, 31, 25, 21, 50]
mergeSort(nums)
print(nums)