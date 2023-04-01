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

// Time: O(9^2) = O(1)
// Space: O(9^2) = O(1)

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> rows[9];
        unordered_set<char> cols[9];
        unordered_set<char> grids[3][3];
        for(int row = 0; row < 9; row++)
        {
            for(int col = 0; col < 9; col++)
            {
                // if '.', skip
                if(board[row][col] == '.')
                {
                    continue;
                }
                // if the sets already contains this value, return false
                if(rows[row].count(board[row][col]) || cols[col].count(board[row][col]) || grids[row / 3][col / 3].count(board[row][col]))
                {
                    return false;
                }
                // else, add to set
                else
                {
                    rows[row].insert(board[row][col]);
                    cols[col].insert(board[row][col]);
                    grids[row / 3][col / 3].insert(board[row][col]);
                }
            }
        }

        // if nothing caused false by end the board is good
        return true;
    }
};
