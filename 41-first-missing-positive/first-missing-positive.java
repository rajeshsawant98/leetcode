class Solution {
    public int firstMissingPositive(int[] nums) {
        Map<Integer,Integer> map= new HashMap<>();
        int max= Integer.MIN_VALUE;

        for(int i=0;i<nums.length;i++){
            if(nums[i]>max){
                max=nums[i];
            }
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        }

        int j=2;

        if(max==1){
            return 2;
        }

        if(map.containsKey(1)){
            while(j<=max)
            {
                if(j==max){
                    return max+1;
                }
                else if(!map.containsKey(j)){
                    return j;
                }
               

                j++;

            }
        }

             return 1;
    }
}