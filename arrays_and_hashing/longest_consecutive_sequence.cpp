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

// Time: O(nlogn), loop through once to make queue with logn insertions and go through queue once
// Space: O(n), store another copy of the list

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // handle 0 case
        if(nums.size() == 0)
        {
            return 0;
        }
        // add to priority queue to sort the list
        priority_queue<int> q;
        for(int i : nums)
        {
            q.push(i);
        }
        // get first num
        int longest = 1;
        int currentLength = 1;
        int last = q.top();
        q.pop();
        // go through in order of size and get longest chain
        while(q.size() > 0)
        {
            // if the current char is 1 less than previous (queue is decreasing)
            if(last - q.top() == 1)
            {
                // update current length
                currentLength++;
                // if this is the longest, keep longest updated as well
                if(currentLength > longest)
                {
                    longest = currentLength;
                }
            }
            // handle duplicate case
            else if(last - q.top() == 0)
            {
                q.pop();
                continue;
            }
            // if the chain is broken reset current length
            else
            {
                currentLength = 1;
            }
            // set last and pop queue
            last = q.top();
            q.pop();
        }
        return longest;
    }
};
