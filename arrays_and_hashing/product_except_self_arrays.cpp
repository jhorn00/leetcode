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

// Time: O(n), loops and performs constant operations 3*n times
// Space: O(n), loops and creates lists 3*n size dependent

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // before current initialized to avoid check
        int* beforeProduct = new int[nums.size()];
        beforeProduct[0] = nums[0];
        for(int current = 1; current < nums.size(); current++)
        {
            // add product of current element with last product to list
            // current - 1 represents last product in beforeProduct vector
            beforeProduct[current] = beforeProduct[current - 1] * nums[current];
        }
        // after current initialized to avoid check
        int* afterProduct = new int[nums.size()];
        afterProduct[nums.size() - 1] = nums[nums.size() - 1];
        for(int current = nums.size() - 2; current >= 0; current--)
        {
            // add product of current element with last product to list
            // last product is the last element of the afterProduct vector
            afterProduct[current] = afterProduct[current + 1] * nums[current];
        }
        // calculate results
        vector<int> results = {afterProduct[1]}; // everything but first
        for(int current = 1; current < nums.size() - 1; current++)
        {
            // product before times product after (-2 excludes product of all and last element, current shifts further to real after product)
            results.push_back(beforeProduct[current - 1] * afterProduct[current + 1]);
        }
        results.push_back(beforeProduct[nums.size() - 2]); // everything but last
        // return
        //clean up memory
        delete[] beforeProduct;
        delete[] afterProduct;
        return results;
    }
};
