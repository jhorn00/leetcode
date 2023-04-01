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

// Time: O(n), loops and performs constant operations 2*n times
// Space: O(1), no extra space on top of return value

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // init vector of n size and fill with 1s
        vector<int> results(nums.size(), 1);
        // init before product as 1 so we can multiply
        int before = 1;
        // for each number, assign result to the product of things before it (for first element this is 1)
        for(int current = 0; current < nums.size(); current++)
        {
            results[current] = before;
            before *= nums[current];
        }
        // init after product as 1 so we can multiply
        int after = 1;
        // for each number, multiply result (product before current number) with the product after the current num
        for(int current = nums.size() - 1; current >= 0; current--)
        {
            results[current] *= after;
            after *= nums[current];
        }
        // return
        return results;
    }
};
