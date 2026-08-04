class Solution {
public:
    int minSwaps(string s) {

        int balance = 0;
        int unmatchedClose = 0;

        for (char ch : s) {

            if (ch == '[') {
                balance++;
            }
            else {

                if (balance > 0)
                    balance--;
                else
                    unmatchedClose++;
            }
        }

        return (unmatchedClose + 1) / 2;
    }
};