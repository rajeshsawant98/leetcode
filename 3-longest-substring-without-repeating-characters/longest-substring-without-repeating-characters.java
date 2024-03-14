class Solution {
    public int lengthOfLongestSubstring(String s) {

        Set<Character> ss = new HashSet<>();

        int l = 0;
        char[] sarr=s.toCharArray();
        int len=0;

        for (int r=0;r<sarr.length;r++)
         {
            while(ss.contains(sarr[r]))
            { 
                ss.remove(sarr[l]);
                l += 1;
            }
            ss.add(sarr[r]);
            len= Math.max(len, r-l+1);

        }
        return len ;

    }
}