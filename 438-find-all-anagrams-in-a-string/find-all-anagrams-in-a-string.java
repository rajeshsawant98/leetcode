
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res = new ArrayList<>();

        if(p.length()>s.length()){
            return res;
        }
        Map<Character, Integer> pCount = new HashMap<>();
        Map<Character, Integer> sCount = new HashMap<>();
        

        // Populate pCount map
        for (char c : p.toCharArray()) {
            pCount.put(c, pCount.getOrDefault(c, 0) + 1);
        }

        int pLength = p.length();

        // Initialize sCount for the first window
        for (int i = 0; i < pLength; i++) {
            char c = s.charAt(i);
            sCount.put(c, sCount.getOrDefault(c, 0) + 1);
        }

        // Compare initial window
        if (sCount.equals(pCount)) {
            res.add(0);
        }

        // Move the window and compare counts
        for (int i = pLength; i < s.length(); i++) {
            char leftChar = s.charAt(i - pLength); // Character going out of the window
            char rightChar = s.charAt(i); // Character coming into the window

            // Update counts for the new window
            sCount.put(rightChar, sCount.getOrDefault(rightChar, 0) + 1);
            sCount.put(leftChar, sCount.get(leftChar) - 1);

            // Remove if count becomes 0
            if (sCount.get(leftChar) == 0) {
                sCount.remove(leftChar);
            }

            // Compare counts and add index to result if match found
            if (sCount.equals(pCount)) {
                res.add(i - pLength + 1);
            }
        }

        return res;
    }
}
