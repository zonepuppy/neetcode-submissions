class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1 = {}
        for i in range(len(nums)):
            list1[nums[i]] = i
        for j in range(len(nums)):
            value = target - nums[j]
            if value in list1 and list1[value] != j:
                if list1[value] < j:
                    a = list1[value]
                    b = j
                else:
                    a = j
                    b = list1[value]
                return [a, b]
                        