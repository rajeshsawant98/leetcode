class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = set()

        total = 0

        max_sum = 0

        left = 0

        for right in range(len(nums)):

            # Remove elements until nums[right] becomes distinct

            while nums[right] in window:

                window.remove(nums[left])

                total -= nums[left]

                left += 1

            window.add(nums[right])

            total += nums[right]

            # Keep the window length at most k

            if right - left + 1 > k:

                window.remove(nums[left])

                total -= nums[left]

                left += 1

            # Valid window: length k and all elements distinct

            if right - left + 1 == k:

                max_sum = max(max_sum, total)

        return max_sum