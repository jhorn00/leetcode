// These will probably end up with a ton of includes for the sake of saving time
// I am not going to be organizing the includes

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <set>
#include <unordered_map>
#include <stack>

// for leetcode :(
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // same length? might not have to check characters
        if(s.size() != t.size())
        {
            return false;
        }
        // sorting is easiest
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        // if same it is anagram
        if(s != t)
        {
            return false;
        }
        return true;
    }
};
