from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0

        for candie in candies:
            max_candies = max(candie, max_candies)

        result = []

        for candie in candies:
            is_max_candies = candie + extraCandies >= max_candies
            result.append(is_max_candies)

        return result


if __name__ == "__main__":
    solver = Solution()

    tests = [
        ([2,3,5,1,3], 3),
        ([4,2,1,1,2], 1),
        ([12,1,12], 10)
    ]

    for test_case in tests:
        solution = solver.kidsWithCandies(*test_case)
        print(f"candies are: '{test_case[0]}'")
        print(f"extra candies are: '{test_case[1]}'")
        print(f"solution is: '{solution}'")
        print()
