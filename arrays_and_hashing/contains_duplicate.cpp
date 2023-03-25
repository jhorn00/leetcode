// These will probably end up with a ton of includes for the sake of saving time
// I am not going to be organizing the includes

#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <set>
#include <unordered_map>

// for leetcode :(
using namespace std;

// This is Time: O(n) and Space O(n)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> haveIt;
        for (int i : nums)
        {
            if(haveIt.find(i) != haveIt.end())
            {
                return true;
            }
            haveIt.emplace(i);
        }
        return false;
    }
};