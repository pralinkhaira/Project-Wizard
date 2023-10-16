class Solution {
public:
    vector<int> getRow(int rowIndex) {
        // Initialize a 2D vector to represent Pascal's Triangle
        vector<vector<int>> pascalTriangle(rowIndex + 1);

        // Initialize the first row with a single element '1'
        pascalTriangle[0].push_back(1);

        // Generate the rest of the rows
        for (int currentRow = 1; currentRow <= rowIndex; currentRow++) {
            // The first element of each row is always '1'
            pascalTriangle[currentRow].push_back(1);

            // Get a reference to the current row and the previous row
            vector<int>& currentRowList = pascalTriangle[currentRow];
            vector<int>& previousRowList = pascalTriangle[currentRow - 1];

            // Calculate and populate the middle elements of the row
            for (int j = 1; j < previousRowList.size(); j++) {
                int sum = previousRowList[j] + previousRowList[j - 1];
                currentRowList.push_back(sum);
            }

            // The last element of each row is also '1'
            currentRowList.push_back(1);
        }

        return pascalTriangle[rowIndex];
    }
};
