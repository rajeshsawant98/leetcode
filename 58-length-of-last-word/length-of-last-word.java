class Solution {
    public int lengthOfLastWord(String s) {
        boolean notEmpty = false;
        int l = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) != ' ') {
                notEmpty = true;
                l++;
            } else {
                if (notEmpty) {
                    break;
                }
            }
        }
        return l;
    }
}