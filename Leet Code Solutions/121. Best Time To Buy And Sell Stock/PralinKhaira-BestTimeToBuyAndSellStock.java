class Solution {
    // public static int maxProfit(int[] prices) {
    //     int highestProfit = 0;
    //     for (int i = 0; i < prices.length; i++) {
    //         for (int j = i+1; j < prices.length; j++) {
    //             int profit = prices[j] - prices[i];
    //             if (profit > highestProfit) {
    //                 highestProfit = profit;
    //             }
    //         }
    //     }

    //     return highestProfit;
    // }


    public static int maxProfit(int[] prices) {
        int highestProfit = 0;
        int minPrice = prices[0];

        for (int i = 0; i < prices.length; i++) {
            int profit = prices[i] - minPrice;
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }

            if (profit > highestProfit) {
                highestProfit = profit;
            }
        }

        return highestProfit;
    }


    public static void main(String[] args) {
        int[] a = {7,1,5,3,6,4};
        System.out.println(maxProfit(a));
    }
}