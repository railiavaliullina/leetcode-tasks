class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] == nums[i]:
                del nums[i]
            else:
                i += 1
        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates(nums=[1, 1]))
    print(sol.removeDuplicates(nums=[2, 2, 2, 2, 3, 3, 4, 5]))

