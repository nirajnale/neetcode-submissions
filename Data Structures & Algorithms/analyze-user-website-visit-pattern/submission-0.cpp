class Solution {
public:
    vector<string> mostVisitedPattern(vector<string>& username,
                                      vector<int>& timestamp,
                                      vector<string>& website) {

        int n = username.size();

        vector<tuple<int, string, string>> visits;

        for (int i = 0; i < n; i++) {
            visits.push_back({timestamp[i], username[i], website[i]});
        }

        sort(visits.begin(), visits.end());

        unordered_map<string, vector<string>> userVisits;

        for (auto& [time, user, site] : visits) {
            userVisits[user].push_back(site);
        }

        map<vector<string>, int> patternCount;

        for (auto& [user, sites] : userVisits) {

            set<vector<string>> seen;

            int m = sites.size();

            for (int i = 0; i < m; i++) {
                for (int j = i + 1; j < m; j++) {
                    for (int k = j + 1; k < m; k++) {

                        vector<string> pattern = {
                            sites[i],
                            sites[j],
                            sites[k]
                        };

                        seen.insert(pattern);
                    }
                }
            }

            for (auto& pattern : seen) {
                patternCount[pattern]++;
            }
        }

        vector<string> answer;
        int best = 0;

        for (auto& [pattern, cnt] : patternCount) {

            if (cnt > best) {
                best = cnt;
                answer = pattern;
            }
        }

        return answer;
    }
};