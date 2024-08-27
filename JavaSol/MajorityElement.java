class Solution {
    public int majorityElement(int[] nums) {
        
        int arrLength = nums.length;
        int majorityCount =  arrLength / 2;
        java.util.HashMap<Integer, Integer> countNums = new java.util.HashMap<>();

        for (int i = 0; i < arrLength; i++ ){
            countNums.merge(nums[i], 1, Integer::sum);
            if (countNums.get(nums[i]) > majorityCount) {
                return nums[i];
            }
        }
    return -1;
    }
}