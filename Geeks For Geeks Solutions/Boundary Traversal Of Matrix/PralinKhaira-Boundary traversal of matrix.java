/*
Boundary traversal of matrix
Link Of Problem - https://practice.geeksforgeeks.org/problems/boundary-traversal-of-matrix-1587115620/1
*/

class Solution
{
    static ArrayList<Integer> boundaryTraversal(int matrix[][], int n, int m)
    {
         ArrayList<Integer> result = new ArrayList<>();

        if (n == 1) {
            for (int i = 0; i < m; i++) {
                result.add(matrix[0][i]);
            }
        } else if (m == 1) {
            for (int i = 0; i < n; i++) {
                result.add(matrix[i][0]);
            }
        } else {
            for (int i = 0; i < m; i++) {
                result.add(matrix[0][i]);
            }
            for (int i = 1; i < n; i++) {
                result.add(matrix[i][m - 1]);
            }
            if (n > 1) {
                for (int i = m - 2; i >= 0; i--) {
                    result.add(matrix[n - 1][i]);
                }
            }
            if (m > 1) {
                for (int i = n - 2; i > 0; i--) {
                    result.add(matrix[i][0]);
                }
            }
        }
        return result;
    }
}
