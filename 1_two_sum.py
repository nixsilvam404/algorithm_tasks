def sum(nums: list, target: int):
    answer = []
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums[i+1:]:
            answer.extend([i, nums[i+1:].index(diff)+i+1])
    return answer

print(sum([2,7,11,15], 9))
print(sum([3,2,4], 6))
print(sum([3,3], 6))