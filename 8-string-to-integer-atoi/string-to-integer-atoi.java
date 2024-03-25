class Solution {
    public int myAtoi(String s) {
        if (s == null || s.length() == 0)
            return 0;
        
        // Trim leading whitespace
        s = s.trim();
        
        if (s.length() == 0)
            return 0;
        
        // Check for sign
        int sign = 1;
        int i = 0;
        if (s.charAt(i) == '+' || s.charAt(i) == '-') {
            sign = (s.charAt(i) == '-') ? -1 : 1;
            i++;
        }
        
        // Read digits until non-digit or end of string
        long result = 0; // Use long to handle overflow
        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            result = result * 10 + (s.charAt(i) - '0');
            
            // Check for overflow
            if (sign == 1 && result > Integer.MAX_VALUE)
                return Integer.MAX_VALUE;
            if (sign == -1 && -result < Integer.MIN_VALUE)
                return Integer.MIN_VALUE;
            
            i++;
        }
        
        // Apply sign and return result
        return (int)(result * sign);
    }
}
