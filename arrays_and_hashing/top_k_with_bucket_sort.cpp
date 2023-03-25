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
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // count occurances
        unordered_map<int, int> m;
        for(int i = 0; i < nums.size(); i++)
        {
            // if it is in map already
            if(m.count(nums[i]))
            {
                m[nums[i]]++;
            }
            // if first occurance
            else
            {
                m[nums[i]] = 1;
            }
        }
        // create vector to hold occurances and bucket sort
        vector<vector<int>> v(nums.size());
        for(auto itr = m.begin(); itr != m.end(); itr++)
        {
            // second is the number of occurances, first is the number
            v[itr->second - 1].push_back(itr->first);
        }
        // create return value
        vector<int> ret;
        // work backwards k times
        int i = nums.size() - 1;
        int count = 0;
        // risk of OoB, but the problem criteria means it should be fine
        while(count < k && i >= 0)
        {
            // if the occurance vector is not empty, append
            if(!v[i].empty())
            {
                ret.insert(ret.end(), v[i].begin(), v[i].end());
                count = count + v[i].size();
            }
            i--;
        }
        return ret;
    }
};
