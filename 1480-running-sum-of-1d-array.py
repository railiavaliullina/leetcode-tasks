"""
Description:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""


class Solution(object):
    @staticmethod
    def running_sum(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        sum_at_step = nums[0]
        running_sum = [sum_at_step]
        for i in range(1, n):
            running_sum.append(running_sum[i - 1] + nums[i])
        return running_sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.running_sum([1, 2, 3, 4]))
    print(solution.running_sum([1, 1, 1, 1, 1]))
    print(solution.running_sum([3, 1, 2, 10, 1]))
