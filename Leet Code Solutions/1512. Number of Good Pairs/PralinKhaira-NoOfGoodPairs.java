/*
Problem link: https://leetcode.com/problems/number-of-good-pairs/
*/

class Solution {
        public int numIdenticalPairs(int[] A) {
        int ans = 0, cnt[] = new int[101];
        for (int a: A) {
            ans += cnt[a]++;
        }
        return ans;
    }
}
