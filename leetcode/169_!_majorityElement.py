# Boyer-Moore Majority Vote Algorithm 

from collections import Counter


def majorityElement(nums: list[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate



print(majorityElement([2,2,1,1,1,2,2]))
