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

// for leetcode :(
using namespace std;

// Time complexity is O(n^2logn) in the worst case since we loop over the strings n times and for each iteration
// a sort is performed with O(nlogn) worst-case performance. After that another loop of O(n) is done.
// Space complexity is O(n) (ignoring the sort) since the data stored in the map and the return vector should
// scale linearly with n. There might be some weirdness with how many anagrams are present in the list,
// which might result in greater or fewer keys, though the map and return vectors
// still store a single copy of each string. I think that the number of keys (anagrams) in the map is
// somewhat irrelevant to the space complexity since it would likely result in O(n + logn) = O(n).
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // return vector
        vector<vector<string>> ret;
        // attempting a map solution
        unordered_map<string, vector<string>> anagrams;
        for(string i : strs)
        {
            // sort the string (copy, not original)
            string sortMe = i;
            sort(sortMe.begin(), sortMe.end());
            // if we have it already, push original back
            if(anagrams.count(sortMe))
            {
                anagrams[sortMe].push_back(i);
            }
            // if this is a new character set create the map element
            else
            {
                anagrams[sortMe] = {i};
            }
        }
        // create return value
        for(auto i = anagrams.begin(); i != anagrams.end(); i++)
        {
            ret.push_back(i->second);
        }
        return ret;
    }
};
