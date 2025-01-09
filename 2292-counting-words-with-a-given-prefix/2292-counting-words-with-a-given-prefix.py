class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        for i in range(len(words)):
            words[i] = words[i][:len(pref)]
        return words.count(pref)
