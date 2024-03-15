class Solution {
    public int longestConsecutive(int[] nums) {

         if (nums == null || nums.length == 0)
            return 0;
        Map<Integer, Boolean> map = new HashMap<>();

        for (int i : nums) {
            if (!map.containsKey(i)) {
                map.put(i, false);
            }
        }
        int longest = 1;

        for (int j : map.keySet()) {
            if (map.get(j) == false) {
                int temp = 1 ;
                int f = j;
                while (map.containsKey(j - 1) && !map.get(j - 1)) {
                    temp++;
                    map.put(j - 1, true);
                    j--;
                }

                while (map.containsKey(f + 1) && !map.get(f + 1)) {
                    temp++;
                    map.put(f + 1, true);
                    f++;
                }
                longest = Math.max(longest, temp);
            }
        }
        return longest ;
    }
}