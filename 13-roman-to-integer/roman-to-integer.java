class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> map= new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);

        char[] c=s.toCharArray();

        int num=0;

        for(int i=c.length-1;i>=0;i--){
            if(i==c.length-1){
                num+=map.get(c[i]);
            }
            else if(map.get(c[i])<map.get(c[i+1])){
                num-=map.get(c[i]);
            }
            else {
                num+=map.get(c[i]);
            }
        }
        return num;
    }
}