class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {

        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {

            // Find an odd number on the left
            while (left < right && nums[left] % 2 == 0) {
                left++;
            }

            // Find an even number on the right
            while (left < right && nums[right] % 2 == 1) {
                right--;
            }

            // Swap odd on left with even on right
            if (left < right) {
                swap(nums[left], nums[right]);
                left++;
                right--;
            }
        }

        return nums;
    }
};