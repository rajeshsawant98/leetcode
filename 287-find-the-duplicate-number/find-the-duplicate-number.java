class Solution {
    public int findDuplicate(int[] nums) {
    boolean [] isPresent = new boolean[nums.length+1];
    for(int i:nums){
        if(isPresent[i]){
            System.gc();
            return i;
        }
        else {
            isPresent[i]=true;
        }
     }
      System.gc();
     return -1;
    }
}