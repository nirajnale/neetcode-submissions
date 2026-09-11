class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> score(n + 1, 0);

        for (auto& t : trust) {
            int a = t[0];
            int b = t[1];

            score[a]--;  // a trusts someone
            score[b]++;  // b is trusted by someone
        }

        for (int person = 1; person <= n; person++) {
            if (score[person] == n - 1) {
                return person;
            }
        }

        return -1;
    }
};