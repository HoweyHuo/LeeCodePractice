class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        return Solution.deDupChars([s])

    @staticmethod
    def deDupChars(deDupList):
        noDupChar = False
        longest = 1
        for deDupStr in deDupList:
            char_pos_list = Solution.deDupWalk(deDupStr)
            if len(char_pos_list) > 1:
                deDupStrList = Solution.deDupSubStr(char_pos_list, deDupStr)
                new_longest = Solution.deDupChars(deDupStrList) if len(deDupStrList) > 0 else 0
            else:
                new_longest = len(deDupStr)
            if new_longest > longest:
                longest = new_longest
        return longest

    @staticmethod
    def deDupSubStr(char_pos_list, s):
        str_len = len(s)
        char_pos_list.insert(0, 0)
        char_pos_list.append(None)
        char_str_list = []
        for idx in range(0, len(char_pos_list) - 2):
            start_idx = char_pos_list[idx]
            end_idx = char_pos_list[idx + 2]
            if end_idx is None:
                sub_str = s[start_idx + 1:]
            else:
                sub_str = s[start_idx:end_idx]
            if len(sub_str) > 1:
                char_str_list.append(sub_str)
        return char_str_list

    @staticmethod
    def deDupWalk(char_str):
        char_pos_hash = {}
        most_char_count = 0
        most_char = None
        for char_idx in range(0, len(char_str)):
            idx_char = char_str[char_idx]
            char_pos_hash.setdefault(idx_char, [])
            char_pos_hash[idx_char].append(char_idx)
            char_count = len(char_pos_hash[idx_char])
            if char_count > most_char_count:
                most_char_count = char_count
                most_char = idx_char
        return char_pos_hash[most_char]


class Solution2(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_len = len(s) if s is not None else 0
        if str_len < 2:
            return str_len
        char_map = {}
        start_idx = 0
        start_char = s[start_idx]
        char_map[start_char] = start_idx
        end_idx = 0
        longest = 1
        while True:
            end_idx += 1
            if end_idx < str_len:
                end_char = s[end_idx]
                if end_char in char_map:
                    start_idx = char_map[end_char] + 1
                char_map[end_char] = end_idx
                sub_str_len = end_idx - start_idx + 1
                if sub_str_len > longest:
                    longest = sub_str_len
            else:
                break
        return longest


s = Solution2()
len = s.lengthOfLongestSubstring("abcabcbb")
print(len)
