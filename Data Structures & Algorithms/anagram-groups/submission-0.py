class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for value in strs:
            sorted_value = ''.join(sorted(value))
           
            if sorted_value in hashmap:
                hashmap[sorted_value].append(value)
            

            else:
                hashmap[sorted_value] = [value]

        ans = []
        for key in hashmap:
            ans.append(hashmap[key])
        return ans