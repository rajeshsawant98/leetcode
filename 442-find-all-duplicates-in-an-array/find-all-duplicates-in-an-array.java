class Solution {
    public List<Integer> findDuplicates(int[] nums) {
       
        List<Integer> res=new ArrayList<>();

        for(int i:nums){
           i=Math.abs(i);

           if(nums[i-1]<0){
            res.add(i);
           }
           
           nums[i-1] = -nums[i-1];

        }

        return res;
    }
}