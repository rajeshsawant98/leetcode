class Solution {
    public int missingNumber(int[] nums) {

        Map<Integer,Integer> map= new HashMap<>();

        int c=0;

        for(int i:nums){
            map.put(i,c);
            c++;           
           }

           for(int j=0;j<=nums.length;j++){
            if(!map.containsKey(j)){
                return j;
            }
           }

           return 0;
        
    }
}