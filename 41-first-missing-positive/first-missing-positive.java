class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        
        // Step 1: Mark non-positive integers and numbers greater than n as irrelevant
        for (int i = 0; i < n; i++) {
            if (nums[i] <= 0 || nums[i] > n) {
                nums[i] = n + 1;
            }
        }
        
        // Step 2: Use the array indices as markers to indicate presence of a number
        for (int i = 0; i < n; i++) {
            int num = Math.abs(nums[i]);
            if (num <= n) {
                nums[num - 1] = -Math.abs(nums[num - 1]);
            }
        }
        
        // Step 3: Find the first index not marked
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                return i + 1;
            }
        }
        
        // Step 4: If all indices are marked, return n + 1
        return n + 1;
    }
}
