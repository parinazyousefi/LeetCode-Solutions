class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + ((high - low // 2))
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1

        return -1


#  nums = [-1,0,3,5,9,12], target = 9
#                l     h
