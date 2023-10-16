class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize a list of lists to represent Pascal's Triangle
        pascal_triangle = [[] for _ in range(rowIndex + 1)]
        
        # Initialize the first row with a single element '1'
        pascal_triangle[0].append(1)
        
        # Generate the rest of the rows
        for current_row in range(1, rowIndex + 1):
            # The first element of each row is always '1'
            pascal_triangle[current_row].append(1)
            
            # Calculate and populate the middle elements of the row
            for j in range(1, len(pascal_triangle[current_row - 1])):
                sum_val = pascal_triangle[current_row - 1][j] + pascal_triangle[current_row - 1][j - 1]
                pascal_triangle[current_row].append(sum_val)
                
            # The last element of each row is also '1'
            pascal_triangle[current_row].append(1)
        
        return pascal_triangle[rowIndex]
