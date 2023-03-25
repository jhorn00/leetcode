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

// O(n) for time and memory where n is the size of nums
// We should pass over the list a max of 1 time, giving n time
// We should see an unordered_map with at most n-1 pairs
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // generate map
        unordered_map<int, int> m;
        for(int i = 0; i < nums.size(); i++)
        {
            // if we have target - current
            if(m.count(target - nums[i]))
            {
                return {i, m[target - nums[i]]};
            }
            // if we do not have current
            if(!m.count(nums[i]))
            {
                m[nums[i]] = i;
            }
        }
        return {0, 0};
    }
};
