def bubbleSort(nums):
    for passnum in range(len(nums)-1,0,-1):
        for i in range(passnum):
            if nums[i]>nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

nums = [14,6,23,87,57,31,25,21,50]
bubbleSort(nums)
print(nums)