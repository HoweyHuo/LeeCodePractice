class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        str1_pt = [-1, 0]
        str2_pt = [-1, 0]
        while True:
            has_next1 = Solution.move_pt(word1, str1_pt)
            has_next2 = Solution.move_pt(word2, str2_pt)
            if has_next1 != has_next2:
                return False
            if not has_next1:
                break
            print("word: {0} @{1},{2}".format(word1[str1_pt[0]], str1_pt[0], str1_pt[1]))
            str1_char = Solution.get_char(word1, str1_pt)
            print("word: {0} @{1},{2}".format(word2[str2_pt[0]], str2_pt[0], str2_pt[1]))
            str2_char = Solution.get_char(word2, str2_pt)
            if str1_char != str2_char:
                return False
        return True

    @staticmethod
    def move_pt(word_list, pt):
        if pt[0] == -1:
            pt[0] = 0
            return True
        word = word_list[pt[0]]
        pt[1] += 1
        if pt[1] < len(word):
            return True
        pt[0] += 1
        pt[1] = 0
        if pt[0] < len(word_list):
            return True
        return False

    @staticmethod
    def get_char(word_list, pt):
        return word_list[pt[0]][pt[1]]
