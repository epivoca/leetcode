from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int):
        count = 0
        i = 0

        while i < len(flowerbed) and count < n:
            # Check if the current plot is empty.
            if flowerbed[i] == 1:
                i += 1
                continue

            # Check if the left and right plots are empty.
            empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            # If both plots are empty, we can plant a flower here.
            if empty_left_plot and empty_right_lot:
                flowerbed[i] = 1
                count += 1
                i += 2
            else:
                i += 1

        return count >= n


if __name__ == "__main__":
    solver = Solution()

    tests = [
        ([1,0,0,0,1], 1),
        ([1,0,0,0,1], 2)
    ]

    for test_case in tests:
        solution = solver.canPlaceFlowers(*test_case)
        print(f"flowerbed: '{test_case[0]}'")
        print(f"extra flowers: '{test_case[1]}'")
        print(f"result: '{solution}'")
        print()
