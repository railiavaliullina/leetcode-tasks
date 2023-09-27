class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while n > 0 and m > 0:
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

        print(nums1)


if __name__ == '__main__':
    sol = Solution()
    sol.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
    sol.merge(nums1=[1], m=1, nums2=[], n=0)
    sol.merge(nums1=[0], m=0, nums2=[1], n=1)
    sol.merge(nums1=[2, 0], m=1, nums2=[1], n=1)
    sol.merge(nums1=[4, 5, 6, 0, 0, 0], m=3, nums2=[1, 2, 3], n=3)
    sol.merge([0, 0, 0, 0, 0], m=0, nums2=[1, 2, 3, 4, 5], n=5)
    sol.merge(nums1=[4, 0, 0, 0, 0, 0], m=1, nums2=[1, 2, 3, 5, 6], n=5)
