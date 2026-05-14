class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // sliding window

        // maintain window size of k

        Set<Integer> window = new HashSet<>();
        int l = 0;

        for (int r = 0; r < nums.length; r++) {
            while (r - l > k) {
                window.remove(nums[l]);
                l ++;
            }

            if (!window.add(nums[r])) {
                return true;
            }

        }

        return false;
        
    }
}