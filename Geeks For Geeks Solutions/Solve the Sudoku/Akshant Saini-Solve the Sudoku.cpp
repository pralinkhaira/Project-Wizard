/*
Solve the Sudoku
Problem Link: https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1
*/


class Solution 
{
public:
    bool isvalid(int grid[N][N],int row,int col,int val)
    {
        for(int i=0;i<9;i++)
        {
            if(grid[i][col]==val)
                return false;
            if(grid[row][i]==val)
                return false;
            if(grid[3* (row/3) +i/3][3*(col/3)+ i%3]==val)
                return false;
        }
        return true;
    }
    
    
    bool SolveSudoku(int grid[N][N])  
    { 
        // Your code here
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                if(grid[i][j]==0)
                {
                    for(int val=1;val<=9;val++)
                    {
                        if(isvalid(grid,i,j,val))
                        {
                            grid[i][j]=val;
                            if(SolveSudoku(grid)==true)
                                return true;
                            else
                               grid[i][j]=0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
    //Function to print grids of the Sudoku.
    void printGrid (int grid[N][N]) 
    {
        // Your code here 
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                cout<<grid[i][j]<<" ";
            }
           // cout<<endl;
        }
    }
};
     
