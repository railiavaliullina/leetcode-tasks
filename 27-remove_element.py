class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        j = n - 1
        for i in range(n):
            if nums[i] == val:
                while j != i:
                    if nums[j] == val:
                        nums[j] = None
                        j -= 1
                    else:
                        nums[i] = nums[j]
                        nums[j] = None
                        j -= 1
                        break
                if j == i and nums[i] == val:
                    nums[i] = None

        return len([num for num in nums if num is not None])


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeElement(nums=[1], val=1))
    print(sol.removeElement(nums=[3, 3], val=3))
    print(sol.removeElement(nums=[4, 5], val=4))
    print(sol.removeElement(nums=[3, 2, 2, 3], val=3))
    print(sol.removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
