from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

a = Solution()
print(a.twoSum([2,11,7,15], 9))


"""
To solve this problem, first create an empty hash map to store values
loop through the input list 'nums' and get the answer of this expression "target - element at index 'i' of nums"
save the index if the answer to the expression to the hash map.
check if the answer to that expression is in the hash map that was created
return [value, i]
"""