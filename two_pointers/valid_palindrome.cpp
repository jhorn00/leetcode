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

// This type of solution is supposedly O(n) for both.
// Assuming insert or other functions aren't adding to it, I think that is correct.

class Solution {
public:
    bool isAlphanumeric(char c)
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
