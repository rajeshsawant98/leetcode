class Solution {
    public int lengthOfLongestSubstring(String s) {

        char[] sarr=s.toCharArray();
        int longest=0;
        int l=0;

        Set<Character> hs= new HashSet<>();
        for (int r=0;r<sarr.length;r++)
        {
            while(hs.contains(sarr[r])){
                hs.remove(sarr[l]);
                l++;
            }
            hs.add(sarr[r]);
            longest=Math.max(longest,r-l+1);

        }
        return longest;
    }
}