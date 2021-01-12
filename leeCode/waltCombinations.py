import json
import copy


class Solution(object):
    arr = []
    combinations = []

    def countArrangement(self, n: int) -> int:
        for i in range(0, n):
            self.arr.append(i+1)
        self.walk()
        return len(self.combinations)

    def walk(self, current_arr=None):
        if current_arr is None:
            current_arr = []
        if len(current_arr) == len(self.arr):
            new_arr = copy.deepcopy(current_arr)
            self.combinations.append(new_arr)
            return
        for idx in range(0, len(self.arr)):
            idx_value = self.arr[idx]
            next_idx = len(current_arr) + 1
            if idx_value not in current_arr and (next_idx % idx_value == 0 or idx_value % next_idx == 0):
                current_arr.append(idx_value)
                self.walk(current_arr)
                current_arr.pop()

    def display(self):
        print("combination count: {0}".format(len(self.combinations)))
        print(json.dumps(self.combinations))

    def validate(self):
        for arr in self.combinations:
            for idx in range(0, len(arr)):
                i = idx + 1
                assert arr[idx] %i == 0 or i % arr[idx] == 0, "array failed validation".format(arr)


tree_walker = Solution()
output = tree_walker.countArrangement(1)
print("input 1")
print("output: {0}".format(output))
tree_walker.display()
tree_walker.validate()

