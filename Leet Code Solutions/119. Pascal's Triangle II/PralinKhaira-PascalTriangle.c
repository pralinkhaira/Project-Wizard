int* getRow(int rowIndex, int* returnSize) {
    // Initialize a 2D array to represent Pascal's Triangle
    int** pascalTriangle = (int**)malloc((rowIndex + 1) * sizeof(int*));
    
    for (int i = 0; i <= rowIndex; i++) {
        pascalTriangle[i] = (int*)malloc((i + 1) * sizeof(int));
    }
    
    // Generate the rows
    for (int currentRow = 0; currentRow <= rowIndex; currentRow++) {
        pascalTriangle[currentRow][0] = 1;  // The first element of each row is always '1'
        
        if (currentRow > 0) {
            int* previousRow = pascalTriangle[currentRow - 1];
            
            // Calculate and populate the middle elements of the row
            for (int j = 1; j < currentRow; j++) {
                pascalTriangle[currentRow][j] = previousRow[j] + previousRow[j - 1];
            }
            
            pascalTriangle[currentRow][currentRow] = 1;  // The last element of each row is also '1'
        }
    }
    
    // Set the return size
    *returnSize = rowIndex + 1;
    
    // Copy the row to a 1D array
    int* resultRow = (int*)malloc((rowIndex + 1) * sizeof(int));
    for (int i = 0; i <= rowIndex; i++) {
        resultRow[i] = pascalTriangle[rowIndex][i];
    }
    
    return resultRow;
}
