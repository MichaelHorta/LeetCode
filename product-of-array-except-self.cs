public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] prefixes = new int[nums.Length];
        prefixes[0]=1;
        int[] suffixes = new int[nums.Length];
        suffixes[nums.Length-1] = 1;
        for(int i = 1; i < nums.Length; i++){
            prefixes[i] = nums[i-1]*prefixes[i-1];
            suffixes[nums.Length-1-i] = nums[nums.Length-i]*suffixes[nums.Length-i];
        }

        int[] prods = new int[nums.Length];
        for(int i = 0; i < nums.Length; i++){
            prods[i] = prefixes[i] * suffixes[i];
        }

        return prods;
    }
}