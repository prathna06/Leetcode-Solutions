from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)
        char_counts = dict(sorted(char_counts.items(), key=lambda item: -item[1]))
        new_string = ""
        for i in range(len(s)):
            keys = list(char_counts.keys())
            if (not new_string or new_string[-1] != keys[0]) and char_counts[keys[0]] > 0:
                new_string += keys[0]
                char_counts[keys[0]] -= 1
                if len(keys) > 1 and char_counts[keys[0]] < char_counts[keys[1]]:
                    char_counts = dict(sorted(char_counts.items(), key=lambda item: -item[1]))
            elif len(keys) < 2 or char_counts[keys[1]] == 0:
                return ""
            else:
                new_string += keys[1]
                char_counts[keys[1]] -= 1
                if len(keys) > 2 and char_counts[keys[1]] < char_counts[keys[2]]:
                    char_counts = dict(sorted(char_counts.items(), key=lambda item: -item[1]))
        return new_string