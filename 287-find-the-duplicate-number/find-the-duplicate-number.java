class Solution {
    public int findDuplicate(int[] nums) {
        boolean[] vis = new boolean[nums.length+1];
        for(int i:nums){
            if(vis[i] == false){
                vis[i] = true;
            }
           else{ return i;}
        }
        return -1;
    }
}