import os
import json

class Solution1:
    def createSortedArray(self, instructions) -> int:
        nums = []
        total_cost = 0
        countMap = {}
        for idx in range(0, len(instructions)):
            number = instructions[idx]
            if number in countMap:
                countMap[number]["count"] += 1
            else:
                countMap[number] = {
                    "count": 1
                }
                if len(nums) == 0 or number > nums[-1]:
                    nums.append(number)
                    if len(nums) > 1:
                        last_num = nums[len(nums) - 2]
                        countMap[number]["pre"] = last_num
                        countMap[last_num]["next"] = number
                    continue
                if number < nums[0]:
                    nums.insert(0, number)
                    countMap[number]["next"] = nums[1]
                    countMap[nums[1]]["pre"] = number
                    continue
                Solution.sortInsert(nums, number, countMap)
            total_cost += Solution.calcCost(countMap, number, idx + 1)
        return total_cost

    @staticmethod
    def sortInsert(nums, number, count_map, scope_start=0, scope_end=None):
        if scope_end is None:
            scope_end = len(nums) - 1
        scope_len = scope_end - scope_start + 1
        if scope_len == 2:
            pre_num = nums[scope_start]
            next_num = nums[scope_start + 1]
            nums.insert(scope_start + 1, number)
            count_map[pre_num]["next"] = number
            count_map[next_num]["pre"] = number
            count_map[number]["pre"] = pre_num
            count_map[number]["next"] = next_num
            return
        mid_idx = scope_start + scope_len // 2
        mid_val = nums[mid_idx]
        if mid_val > number:
            return Solution.sortInsert(nums, number, count_map, scope_start, mid_idx)
        else:
            return Solution.sortInsert(nums, number, count_map, mid_idx, scope_end)

    @staticmethod
    def calcCost(count_map, number, num_len):
        num_meta = count_map[number]
        right_cost = 0
        while "next" in num_meta:
            num_meta = count_map[num_meta["next"]]
            right_cost += num_meta["count"]
        left_cost = num_len - right_cost - count_map[number]["count"]
        if left_cost <= right_cost:
            return left_cost
        return right_cost


class Solution2:
    def createSortedArray(self, instructions) -> int:
        nums = []
        total_cost = 0
        for idx in range(0, len(instructions)):
            number = instructions[idx]
            if idx == 0:
                nums.append(number)
                continue
            if nums[0] >= number:
                nums.insert(0, number)
                continue
            if nums[-1] <= number:
                nums.append(number)
                continue
            total_cost += self.insertSort(nums, number, idx)
            # print("number: {0} num: {1}, cost: {2}".format(number, nums, total_cost))
        return total_cost

    def insertSort(self, nums, number, num_len, scope_start=0, scope_end=None):
        if scope_end is None:
            scope_end = num_len - 1
        if scope_start + 1 == scope_end:
            nums.insert(scope_end, number)
            return self.find_cost(nums, scope_end, number, num_len + 1)
        mid_idx = scope_start + (scope_end - scope_start + 1) // 2
        mid_val = nums[mid_idx]
        if mid_val == number:
            nums.insert(mid_idx, number)
            return self.find_cost(nums, mid_idx, number, num_len + 1)
        if mid_val < number:
            return self.insertSort(nums, number, num_len, mid_idx, scope_end)
        return self.insertSort(nums, number, num_len, scope_start, mid_idx)

    def calcCost(self, left_idx, right_idx, num_len):
        left_cost = left_idx + 1
        right_cost = num_len - right_idx
        return min(left_cost, right_cost)

    def find_cost(self, nums, idx, number, num_len):
        left_idx = None
        right_idx = None
        for step in range(1, num_len):
            left = idx - step
            right = idx + step
            if left_idx is None and nums[left] < number:
                left_idx = left
            if right_idx is None and nums[right] > number:
                right_idx = right
            if left_idx is None or right_idx is None:
                continue
            break
        return self.calcCost(left_idx, right_idx, num_len)

class SolutionSample:
    def createSortedArray(self, instructions) -> int:
        n = len(instructions)
        smaller = [0]*n
        larger = [0]*n
        temp = [0]*n  # record some temporal information

        def sort_smaller(arr, left, right):
            if left == right:
                return
            mid = (left + right) // 2
            sort_smaller(arr, left, mid)
            sort_smaller(arr, mid+1, right)
            merge_smaller(arr, left, right, mid)

        def merge_smaller(arr, left, right, mid):
            # merge [left, mid] and [mid+1, right]
            i = left
            j = mid+1
            k = left
            # use temp[left...right] to temporarily store sorted array
            while i <= mid and j <= right:
                if arr[i][0] < arr[j][0]:
                    temp[k] = arr[i]
                    k += 1
                    i += 1
                else:
                    temp[k] = arr[j]
                    smaller[arr[j][1]] += i - left
                    k += 1
                    j += 1

            while i <= mid:
                temp[k] = arr[i]
                k += 1
                i += 1
            while j <= right:
                temp[k] = arr[j]
                smaller[arr[j][1]] += i - left
                k += 1
                j += 1
            # restore from temp
            for i in range(left, right+1):
                arr[i] = temp[i]

        def sort_larger(arr, left, right):
            if left == right:
                return
            mid = (left + right) // 2
            sort_larger(arr, left, mid)
            sort_larger(arr, mid+1, right)
            merge_larger(arr, left, right, mid)

        def merge_larger(arr, left, right, mid):
            # merge [left, mid] and [mid+1, right]
            i = left
            j = mid+1
            k = left
            # use temp[left...right] to temporarily store sorted array
            while i <= mid and j <= right:
                if arr[i][0] <= arr[j][0]:
                    temp[k] = arr[i]
                    k += 1
                    i += 1
                else:
                    temp[k] = arr[j]
                    larger[arr[j][1]] += mid - i + 1
                    k += 1
                    j += 1

            while i <= mid:
                temp[k] = arr[i]
                k += 1
                i += 1
            while j <= right:
                temp[k] = arr[j]
                larger[arr[j][1]] += mid - i + 1
                k += 1
                j += 1
            # restore from temp
            for i in range(left, right+1):
                arr[i] = temp[i]

        MOD = 10**9+7
        cost = 0

        arr_smaller = [[v, i] for i, v in enumerate(instructions)]
        arr_larger = [[v, i] for i, v in enumerate(instructions)]

        sort_smaller(arr_smaller, 0, n-1)
        sort_larger(arr_larger, 0, n-1)

        for i in range(n):
            cost += min(smaller[i], larger[i])
        return cost % MOD


current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir, "data", "sortArrayThruInstru.json")
with open(data_file) as fp:
    a_list = json.load(fp)

s = Solution()
for a in a_list:
    output = s.createSortedArray(a)
    print(output)
