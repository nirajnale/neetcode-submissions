class Solution {
public:
    int countPalindromicSubsequence(string s) {

        vector<int> first(26, -1), last(26, -1);

        for (int i = 0; i < s.size(); i++) {
            int idx = s[i] - 'a';
            if (first[idx] == -1)
                first[idx] = i;
            last[idx] = i;
        }

        int ans = 0;

        for (int c = 0; c < 26; c++) {

            if (first[c] == -1 || first[c] == last[c])
                continue;

            bool seen[26] = {false};

            for (int i = first[c] + 1; i < last[c]; i++) {
                seen[s[i] - 'a'] = true;
            }

            for (int i = 0; i < 26; i++) {
                if (seen[i]) ans++;
            }
        }

        return ans;
    }
};