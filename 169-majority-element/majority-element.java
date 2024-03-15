class Solution {
    public int majorityElement(int[] nums) {

        Map<Integer,Integer> map= new HashMap<>();
        int majorityCount= (int)(nums.length/2+1);
        
        for(int i:nums)
        {
            map.put(i,map.getOrDefault(i,0)+1);
            if(map.get(i)==majorityCount)
            return i;
        }
        return -1;

        

    
        
    }
}