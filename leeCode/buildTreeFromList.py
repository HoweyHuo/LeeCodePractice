import copy
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        copy.de
        wordList.remove(endWord)
        tree_word_list = [endWord]
        level_number = 1
        level_start = 0
        while True:
            children_word = []
            for word_idx in range(level_start, len(tree_word_list)):
                leaf_word = tree_word_list[word_idx]
                if Solution.transformable(leaf_word, beginWord):
                    return level_number + 1
                for transfer_word in wordList:
                    if transfer_word not in children_word and Solution.transformable(transfer_word, leaf_word):
                        children_word.append(transfer_word)
            if len(children_word) == 0:
                return 0
            for word in children_word:
                wordList.remove(word)
            level_number += 1
            level_start = len(tree_word_list)
            tree_word_list.extend(children_word)
        return 0

    @staticmethod
    def transformable(word1, word2):
        diff_count = 0
        for char_idx in range(0, len(word1)):
            if word1[char_idx] != word2[char_idx]:
                diff_count += 1
                if diff_count > 1:
                    return False
        return True