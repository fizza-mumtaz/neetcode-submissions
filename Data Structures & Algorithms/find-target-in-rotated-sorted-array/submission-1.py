
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2
            guess = nums[mid]

            if guess == target:
                return mid

            elif nums[low] <= guess:

                if nums[low] <= target < guess:
                    high = mid - 1
                else:
                    low = mid + 1

            else:

                if guess < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
