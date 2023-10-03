/*
Problem link: https://leetcode.com/problems/number-of-good-pairs/
*/

class Solution {
public:
        int numIdenticalPairs(vector<int>& A) {
        int ans = 0;
        unordered_map<int, int> cnt;
        for (int x: A) {
        ans += cnt[x]++;
        }
        return ans;
    }
};
