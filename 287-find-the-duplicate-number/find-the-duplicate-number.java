class Solution {
    public int findDuplicate(int[] nums) {

        Arrays.sort(nums);
        int l=0;
        int r=1;

        while(r<nums.length){
            if(nums[r]==nums[l])
            {
                return nums[r];
            }
            else if(nums[r]>nums[l])
            r++;
            l++;
    
        }
        return 0;
        
    }
}