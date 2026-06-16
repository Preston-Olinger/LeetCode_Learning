class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list_word3 = []
        longest_word = 0
        i = 0
        if len(word1) > len(word2):
            longest_word = len(word1)
        else:
            longest_word = len(word2)
        while i < longest_word:
            if i < len(word1):
                list_word3.append(word1[i])
            if i < len(word2):
                list_word3.append(word2[i])
            i = i + 1
        result = "".join(list_word3)
        return result
