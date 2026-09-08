class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for number in nums:
            if hashmap.get(number, 0) != 0:
                return True
            hashmap[number] = 1
        return False