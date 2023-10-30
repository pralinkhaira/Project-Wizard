class Solution {
public:
    static bool compare(int a, int b) {
        // Calculate the number of set bits (1s) in the binary representation of a and b
        int bitCountA = __builtin_popcount(a);
        int bitCountB = __builtin_popcount(b);

        // If the number of set bits is the same for a and b, compare them numerically
        if (bitCountA == bitCountB) {
            return a < b;
        }
        
        // Sort by the number of set bits in ascending order
        return bitCountA < bitCountB;
    }
    
    vector<int> sortByBits(vector<int>& arr) {
        // Use the compare function to sort the vector
        sort(arr.begin(), arr.end(), compare);
        
        // Return the sorted vector
        return arr;
    }
};