class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = set()
        left = 0
        right = 0
        max_length = 0
        if len(s) == 0:
            return 0
        while right < len(s):
            if s[right] not in longest:
                longest.add(s[right])
                right += 1
                if len(longest) > max_length:
                    max_length = len(longest)
            else:
                while s[right] in longest:
                    longest.remove(s[left])
                    left += 1
        return max_length