class Solution {
    public int[] sortByBits(int[] arr) {
        // Convert the input integer array to Integer objects for sorting
        Integer[] integerArr = Arrays.stream(arr).boxed().toArray(Integer[]::new);

        // Create a custom comparator to sort by bit count and then numerically
        Comparator<Integer> comparator = new BitCountComparator();

        // Sort the array using the custom comparator
        Arrays.sort(integerArr, comparator);

        // Convert the sorted array back to primitive integers
        int[] sortedArr = Arrays.stream(integerArr).mapToInt(Integer::intValue).toArray();

        return sortedArr;
    }
}

class BitCountComparator implements Comparator<Integer> {
    @Override
    public int compare(Integer a, Integer b) {
        // Compare based on the count of set bits (1s) in the binary representation
        int bitCountA = Integer.bitCount(a);
        int bitCountB = Integer.bitCount(b);

        if (bitCountA == bitCountB) {
            // If bit counts are the same, compare numerically
            return a - b;
        } else {
            // Sort by the number of set bits in ascending order
            return bitCountA - bitCountB;
        }
    }
}