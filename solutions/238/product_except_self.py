import math


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        products = [1] * length

        for i in range(1, length):
            products[i] = products[i - 1] * nums[i - 1]

        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]

        return products


if __name__ == "__main__":
    solver = Solution()

    tests = [
        [1,2,3,4],
        [-1,1,0,-3,3]
    ]

    for test_case in tests:
        solution = solver.productExceptSelf(test_case)
        print(f"input array: '{test_case}'")
        print(f"result: '{solution}'")
        print()
