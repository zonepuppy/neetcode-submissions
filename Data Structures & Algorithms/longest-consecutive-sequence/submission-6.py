class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        ans = []
        ans.append(count)
        for i in range(len(nums)):
            if i == 0:
                count += 1
                if i == len(nums) - 1:
                    ans.append(count)
                continue
            if nums[i] - 1 == nums[i - 1]:
                count +=1
                if i == len(nums) - 1:
                    ans.append(count)
            elif nums[i - 1] == nums[i]:
                if i == len(nums) - 1:
                    ans.append(count)
                continue
            else:
                ans.append(count)
                count = 1
        -1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9

        return max(ans)