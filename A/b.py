def insertionSort(nums):
   for i in range(1, len(nums)):

     currentvalue = nums[i]
     j = i

     while j>0 and nums[j - 1]>currentvalue:
         nums[j]=nums[j - 1]
         j = j-1

     nums[j]=currentvalue

nums = [22, 16, 43, 27, 33, 41, 17, 21, 56]
insertionSort(nums)
print(nums)