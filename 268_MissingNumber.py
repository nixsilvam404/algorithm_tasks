def missingNumber(nums: list[int]) -> int:
    range_nums = len(nums) + 1
    for i in range(range_nums):
        if i not in nums:
            return i
        


print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))