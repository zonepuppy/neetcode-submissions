class Solution:

    def encode(self, strs: List[str]) -> str:
        word_str = ""
        for word in strs:
            word_str += f"{len(word)}#{word}"
        return word_str
        

    def decode(self, s: str) -> List[str]:
        word_list = []
        

        if s == "":
            return []
        index = 0
        while index < len(s):
            word_length = ""
            
            while s[index] != "#":
                word_length += s[index]
                index += 1

            index += 1
            word_length = int(word_length)

            word = s[index:index + word_length]
            word_list.append(word)

            index += word_length

        return word_list
