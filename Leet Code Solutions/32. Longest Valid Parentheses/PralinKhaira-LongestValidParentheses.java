/*
Link to problem: https://leetcode.com/problems/longest-valid-parentheses/description/
*/

class Solution {
    public int longestValidParentheses(String s) {
        
        Stack<Integer> stk = new Stack<>() ;
       if(!s.isEmpty())
        stk.push(0);
        for(int i = 1 ; i< s.length() ;i++){
            if(stk.isEmpty())
                stk.push(i);
           
            else if(s.charAt(stk.peek()) == '(' && s.charAt(i) == ')')
            {

                stk.pop();
            }
            else 
                stk.push(i);
                
        }
       
        if(stk.isEmpty())
        return s.length() ;
        
        if(stk.size()==1 && s.length()!=1 && ((stk.peek()==0)|| (stk.peek()==s.length()-1)))
        return s.length()-1;
      
       
         int max = 0 ;
        int len = s.length() -1;
        while(!stk.isEmpty()){
            int a =stk.pop();
             max = Math.max(len-a,max);
            len = a-1;
            
        }
         
        return Math.max(max,len-0+1) ;
        
    }
}

/*
Runtime 11 ms
Beats 5.31%
Memory 41.8 MB
Beats 58.57%
*/
