class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum_ = -1001
        while sum_ != target:
            sum_ = numbers[left] + numbers[right]
            if sum_ < target:
                left += 1
            if sum_ > target:
                right -= 1
        return [left+1, right+1]
