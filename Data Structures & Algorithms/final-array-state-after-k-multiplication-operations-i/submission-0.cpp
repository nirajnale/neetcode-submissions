class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {

        priority_queue<
            pair<int, int>,
            vector<pair<int, int>>,
            greater<pair<int, int>>
        > pq;

        // Store {value, index}
        for (int i = 0; i < nums.size(); i++) {
            pq.push({nums[i], i});
        }

        // Perform k operations
        while (k--) {

            auto [value, index] = pq.top();
            pq.pop();

            value *= multiplier;

            nums[index] = value;

            pq.push({value, index});
        }

        return nums;
    }
};