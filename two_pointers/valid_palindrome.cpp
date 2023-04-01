// These will probably end up with a ton of includes for the sake of saving time
// I am not going to be organizing the includes

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <set>
#include <unordered_map>
#include <stack>
#include <queue>

// for leetcode :(
using namespace std;

// Time: O(n) since we traverse the string once
// Space: O(1) since I don't store anything other than my two iterators
class Solution {
public:
    bool isAlphanumeric(char &c)
    {
        if((c >= 65 && c <= 90) || (c >= 97 && c <= 122) || (c >= 48 && c <= 57))
        {
            return true;
        }
        return false;
    }

    bool isPalindrome(string s) {
        int i = 0;
        int j = s.size() - 1;
        while(i < j)
        {
            // check if valid char for comparison
            while((i < j) && !isAlphanumeric(s[i]))
            {
                i++;
            }
            while((i < j) && !isAlphanumeric(s[j]))
            {
                j--;
            }
            // make lowercase
            s[i] = tolower(s[i]);
            s[j] = tolower(s[j]);
            if(s[i] != s[j])
            {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};
