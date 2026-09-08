class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count = Counter(t)
        res = ""
        l, r = 0, 0
        isEnd = False

        while r < len(s):
            substring = s[l:(r+1)]
            window_count = Counter(substring)
            window_count.subtract(count)
            isValid = True
            for key in window_count:
                if window_count[key] < 0:
                    r += 1
                    isValid = False
                    break
            if isValid:
                l += 1
                if res == "":
                    res = substring
                elif len(substring) < len(res):
                    res = substring
   

        return res
            