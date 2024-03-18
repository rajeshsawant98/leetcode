class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        
        // Traverse the digits from right to left
        for (int i = n - 1; i >= 0; i--) {
            // Increment the current digit
            digits[i]++;
            // If the digit is less than 10 after increment, no carry, return digits
            if (digits[i] < 10)
                return digits;
            // Otherwise, set the current digit to 0 and continue to next iteration to propagate the carry
            digits[i] = 0;
        }
        
        // If the loop finishes, it means there's still carry left, so we need to add an extra digit
        int[] newDigits = new int[n + 1];
        newDigits[0] = 1; // The most significant digit is 1
        return newDigits;
    }
}
