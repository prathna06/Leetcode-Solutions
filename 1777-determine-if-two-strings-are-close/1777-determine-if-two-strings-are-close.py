class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False
        wordBank1 = { c:0 for c in word1}
        wordBank2 = {c:0 for c in word2}
        for c in word1:
            wordBank1[c] += 1
        for c in word2:
            wordBank2[c] += 1
 
        return wordBank1.keys() == wordBank2.keys() and sorted(wordBank1.values()) == sorted(wordBank2.values())

       
