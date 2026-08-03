class Solution {
public:
    bool isPalindrome(string &str) {

        int left = 0;
        int right = str.size() - 1;

        while (left < right) {

            if (str[left] != str[right])
                return false;

            left++;
            right--;
        }

        return true;
    }

    bool validPalindrome(string s) {

        if (isPalindrome(s))
            return true;

        for (int i = 0; i < s.size(); i++) {

            string temp = s.substr(0, i) + s.substr(i + 1);

            if (isPalindrome(temp))
                return true;
        }

        return false;
    }
};