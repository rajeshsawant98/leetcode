class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

        HashMap<Character,Integer> map= new HashMap<>();

        for(char c : magazine.toCharArray()){

            map.put(c, map.getOrDefault(c,0)+1);
        }

        for(char c1 : ransomNote.toCharArray()) {
            
            if(!map.containsKey(c1) || map.get(c1)==0){
                return false;}
                else{
                map.put(c1, map.get(c1)-1);
            }
        }

    return true;
    }
}