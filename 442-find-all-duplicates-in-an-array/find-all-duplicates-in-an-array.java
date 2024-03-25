class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        
        Set<Integer> set=new HashSet<>();
        List<Integer> res=new ArrayList<>();

        for(int i:nums){
            if(set.contains(i)){
                res.add(i);
            }
            set.add(i);
        }

        return res;
    }
}