class Solution {
    public static boolean isPalindrome(String s) {
        // if(s.isEmpty()) {
        //     return true;
        // }
        // // remove all non-alphanumeric characters
        // s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        // System.out.println(s);
        // String flipped = "";

        // for (int i = 0; i < s.length(); i++) {
        //     flipped += s.charAt(s.length() - i - 1);
        //     if (s.charAt(i) != flipped.charAt(i)) {
        //         return false;
        //     }
        // }
        // return true;

        // faster method - use 2 pointers:
        if(s.isEmpty()) {
            return true;
        }
        // remove all non-alphanumeric characters
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
        int left = 0;
        int right = s.length() -1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama"));
    }
}