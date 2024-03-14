class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {

              return lessThanNoCount(goal, nums) - lessThanNoCount(goal-1, nums);
    }

     public  static int lessThanNoCount(int x, int[]nums){
            if(x<0){
            return 0;
            }

        int l=0;
        int sum=0;
        int counter=0;

        for(int r=0;r<nums.length;r++)
        {
            sum= sum + nums[r];
            while(sum>x){
                sum= sum - nums[l];
                l++;
            }
            counter += (r-l+1);

            
        
        }
        return counter;
        }
        
}