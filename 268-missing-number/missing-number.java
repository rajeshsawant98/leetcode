class Solution {
    public int missingNumber(int[] nums) {
      int sum = 0;
      int exp = (nums.length)*(nums.length+1)/2;

      for(int i: nums){
        sum += i;
      }
    //  System.gc();
      return exp-sum;
    }
}