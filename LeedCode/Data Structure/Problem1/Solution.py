from typing import List
from sortedcontainers import SortedList

class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        info = {}
        for num in nums:
            if num in info:
                info[num] = info[num] + 1
                return True
            else:
                info[num] = 1

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dic = {}
        for index, num in enumerate(nums):
            if num in my_dic and abs(my_dic[num] - index) <= k:
                return True
            my_dic[num] = index
        return False

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        """
        Given an integer array nums and two integers k and t,
        return true if there are two distinct indices i and j in the array
        such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
        :param nums:
        :param k:
        :param t:
        :return: boolean
        """

        slist = SortedList()
        for i, num in enumerate(nums):
            if i > k:
                slist.remove(nums[i - k - 1])
            pos1 = slist.bisect_left(num - t)
            pos2 = slist.bisect_right(num + t)
            if pos2 > pos1:  # this means that there is a number from the range [num-t, num+t] in the window
                return True
            slist.add(num)
        return False


solution = Solution()
# print(solution.containsDuplicate([1, 2, 1, 4, 5, 3, 2]))
# print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(solution.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0))
