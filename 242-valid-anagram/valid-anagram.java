class Solution {
    static HashMap<Character,Integer>makeFreqMap(String str){
        HashMap<Character,Integer>mp = new HashMap<>();
        for(int i=0;i<str.length();i++){
            char ch = str.charAt(i);
            if(!mp.containsKey(ch)){
                mp.put(ch,1);
            }else{
                int CurrFreq = mp.get(ch);
                mp.put(ch,CurrFreq+1);
            }
        }
        return mp;
    }
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())
        return false;
        HashMap<Character,Integer>Mp1 = makeFreqMap(s);
        HashMap<Character,Integer>Mp2 = makeFreqMap(t);
        return Mp1.equals(Mp2);
    }
}