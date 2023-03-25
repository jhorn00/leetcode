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

// I think this would be Time: O(n)
// where n is length of nums, m is length of m, and k is k
// We need to iterate over nums and count occurances, giving n. We need to insert to
// a heap giving us logm, and we must pop the k number of elements, giving k.
// This would be O(n+logm+k), which reduces to O(n)
// I think this would be Space: O(n) assuming the map and queue have linear consumption
// m could be equal to n in our worst case here, making it O(2n) = O(n)

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
        // create heap structure to sort
        priority_queue<pair<int, int>> q;
        for(auto itr = m.begin(); itr != m.end(); itr++)
        {
            q.emplace(itr->second, itr->first);
        }
        // pop what we need into return value and return
        vector<int> ret;
        for(int i = 0; i < k; i++)
        {
            ret.push_back(q.top().second);
            q.pop();
        }
        return ret;
    }
};
