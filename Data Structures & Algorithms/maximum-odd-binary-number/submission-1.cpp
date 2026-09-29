class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int ones = 0;

        for (char c : s) {
            if (c == '1') {
                ones++;
            }
        }

        int zeros = s.size() - ones;

        string result;

        // Put all but one '1' at the front
        result += string(ones - 1, '1');

        // Put all zeros in the middle
        result += string(zeros, '0');

        // One '1' must be at the end to make the number odd
        result += '1';

        return result;
    }
};