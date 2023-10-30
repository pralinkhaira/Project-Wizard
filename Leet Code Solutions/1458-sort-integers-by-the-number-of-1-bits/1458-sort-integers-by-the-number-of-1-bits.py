class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Define a custom comparison key function for sorting
        def custom_sort_key(num):
            # Calculate the number of set bits (1s) in the binary representation of num
            bit_count = bin(num).count('1')
            return (bit_count, num)

        # Sort the input list using the custom comparison key function
        arr.sort(key=custom_sort_key)

        # Return the sorted list
        return arr