class Solution {
    public int findMaxLength(int[] nums) {
        int n = nums.length;
        int[] prefixSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0)
                prefixSum[i + 1] = prefixSum[i] - 1;
            else
                prefixSum[i + 1] = prefixSum[i] + 1;
        }

        int maxLen = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i <= n; i++) {
            if (map.containsKey(prefixSum[i])) {
                maxLen = Math.max(maxLen, i - map.get(prefixSum[i]));
            } else {
                map.put(prefixSum[i], i);
            }
        }

        return maxLen;
    }
}
