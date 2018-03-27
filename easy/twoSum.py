"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


# solution function
def two_sum_solution(nums, target):
    for x in nums:
        for y in nums:
            if x == y:
                continue
            else:
                return [nums.index(x), nums.index(y)]


# test
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    result = two_sum_solution(nums, target)

    assert nums[result[0]] + nums[result[1]] == target