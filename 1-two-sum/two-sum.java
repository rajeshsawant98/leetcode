class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map < Integer, Integer> difference= new HashMap <>();
        for ( int i=0; i<nums.length;i++){
           Integer diffIndex = difference.get(nums[i]);
           if( diffIndex != null){
               return new int[]{diffIndex,i};
           }
           else{
               difference.put(target-nums[i],i);
           }
        }
        return new int[]{};
    }
}