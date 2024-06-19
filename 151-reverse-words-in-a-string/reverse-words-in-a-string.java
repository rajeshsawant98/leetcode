class Solution {
    public String reverseWords(String s) {
        // Step 1: Trim the input string to remove leading and trailing spaces
        s = s.trim();
        char[] c = s.toCharArray();

        // Initialize pointers
        int p1 = c.length - 1;
        int p2 = p1;

        StringBuilder output = new StringBuilder();

        while (p1 >= 0) {
            // Move p1 to the start of the current word
            while (p1 >= 0 && c[p1] != ' ') {
                p1--;
            }
            
            // Append the word from p1+1 to p2 to the output
            if (p1 < p2) {
                if (output.length() > 0) {
                    output.append(' ');
                }
                output.append(s.substring(p1 + 1, p2 + 1));
            }
            
            // Skip spaces between words
            while (p1 >= 0 && c[p1] == ' ') {
                p1--;
            }
            p2 = p1;
        }

        return output.toString();
    }
}
