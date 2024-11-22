class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        int[] result = solution.twoSum(nums, target);
        // Output the result
        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }
}

// Easiet way to solve this problem - optimal method
// Basic ones- two pointers, hash table, sorting
// Two pointers - not suitable for this problem
// Hash table - suitable for this problem
// Sorting - not suitable for this problem
