class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {

        vector<string> ans;
        int n = words.size();
        int i = 0;

        while (i < n) {

            int j = i;
            int wordsLen = 0;

            // Pick as many words as possible
            while (j < n &&
                   wordsLen + words[j].size() + (j - i) <= maxWidth) {
                wordsLen += words[j].size();
                j++;
            }

            int gaps = j - i - 1;
            string line;

            // Last line or single word
            if (j == n || gaps == 0) {

                for (int k = i; k < j; k++) {

                    line += words[k];

                    if (k != j - 1)
                        line += " ";
                }

                line += string(maxWidth - line.size(), ' ');
            }
            else {

                int totalSpaces = maxWidth - wordsLen;
                int baseSpaces = totalSpaces / gaps;
                int extra = totalSpaces % gaps;

                for (int k = i; k < j; k++) {

                    line += words[k];

                    if (k != j - 1) {

                        int spaces = baseSpaces;

                        if (extra > 0) {
                            spaces++;
                            extra--;
                        }

                        line += string(spaces, ' ');
                    }
                }
            }

            ans.push_back(line);
            i = j;
        }

        return ans;
    }
};