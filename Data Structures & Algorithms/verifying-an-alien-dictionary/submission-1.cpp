class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        
        // rank[character] = position in alien alphabet
        vector<int> rank(26);

        for (int i = 0; i < 26; i++) {
            rank[order[i] - 'a'] = i;
        }

        // Compare adjacent words
        for (int i = 0; i < words.size() - 1; i++) {
            string& a = words[i];
            string& b = words[i + 1];

            int len = min(a.size(), b.size());

            bool foundDifferent = false;

            for (int j = 0; j < len; j++) {
                
                if (a[j] != b[j]) {
                    foundDifferent = true;

                    // a's character must come before b's
                    if (rank[a[j] - 'a'] > rank[b[j] - 'a']) {
                        return false;
                    }

                    break;
                }
            }

            // All common characters matched.
            // Then shorter word must come first.
            if (!foundDifferent && a.size() > b.size()) {
                return false;
            }
        }

        return true;
    }
};