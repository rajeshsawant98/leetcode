import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        // Check if the input array is null or empty
        if (nums == null || nums.length == 0)
            return 0;

        // Create a HashMap to store the presence of each number in the input array
        // Key: number, Value: boolean indicating if the number has been visited
        Map<Integer, Boolean> map = new HashMap<>();

        // Populate the HashMap with numbers from the input array
        for (int i : nums) {
            if (!map.containsKey(i)) {
                map.put(i, false); // Mark the number as unvisited
            }
        }

        // Initialize the variable to store the length of the longest consecutive sequence
        int longest = 1;

        // Iterate through the keys in the HashMap
        for (int j : map.keySet()) {
            // Check if the current number has not been visited
            if (map.get(j) == false) {
                int temp = 1; // Temporary variable to store the length of the current consecutive sequence
                int f = j; // Variable to track the current number

                // Check for consecutive numbers smaller than the current number
                while (map.containsKey(j - 1) && !map.get(j - 1)) {
                    temp++; // Increment the length of the consecutive sequence
                    map.put(j - 1, true); // Mark the number as visited
                    j--; // Move to the previous number
                }

                // Reset the current number to its original value
                j = f;

                // Check for consecutive numbers larger than the current number
                while (map.containsKey(f + 1) && !map.get(f + 1)) {
                    temp++; // Increment the length of the consecutive sequence
                    map.put(f + 1, true); // Mark the number as visited
                    f++; // Move to the next number
                }

                // Update the length of the longest consecutive sequence
                longest = Math.max(longest, temp);
            }
        }

        // Return the length of the longest consecutive sequence
        return longest;
    }
}
