class Solution {
public:
    unordered_map<char, unordered_set<char>> adj;
    unordered_map<char, int> visited;
    string res;

    bool dfs(char c) {
        // cycle detected
        if (visited.count(c)) {
            return visited[c];
        }

        visited[c] = true;

        for (char nei : adj[c]) {
            if (dfs(nei)) {
                return true;
            }
        }

        visited[c] = false;
        res.push_back(c);

        return false;
    }

    string foreignDictionary(vector<string>& words) {

        // initialize graph
        for (string word : words) {
            for (char c : word) {
                adj[c];
            }
        }

        // build edges
        for (int i = 0; i < words.size() - 1; i++) {
            string w1 = words[i];
            string w2 = words[i + 1];

            int minLen = min(w1.size(), w2.size());

            // invalid case
            if (w1.size() > w2.size() &&
                w1.substr(0, minLen) == w2.substr(0, minLen)) {
                return "";
            }

            for (int j = 0; j < minLen; j++) {
                if (w1[j] != w2[j]) {
                    adj[w1[j]].insert(w2[j]);
                    break;
                }
            }
        }

        // topological sort
        for (auto& pair : adj) {
            if (dfs(pair.first)) {
                return "";
            }
        }

        reverse(res.begin(), res.end());

        return res;
    }
};