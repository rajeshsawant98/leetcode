class Solution {
    public int missingNumber(int[] nums) {

        Map<Integer,Integer> map= new HashMap<>();
     
        for(int i:nums){
            map.put(i,i);
                   
           }

           for(int j=0;j<=nums.length;j++){
            if(!map.containsKey(j)){
                return j;
            }
           }

           return 0;
        
    }
}