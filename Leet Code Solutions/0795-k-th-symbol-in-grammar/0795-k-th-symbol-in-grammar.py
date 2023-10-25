class Solution:
    def kthGrammar(self, n, k):
        # Initialize a flag to track if the values of k and the first element are the same.
        are_values_same = True

        # Calculate the total number of elements in the nth row, which is 2^(n-1).
        n = 2**(n - 1)

        # Continue until we reach the first row.
        while n != 1:
            # Halve the number of elements in the row.
            n //= 2

            # If k is in the second half of the row, adjust k and toggle the flag.
            if k > n:
                k -= n
                are_values_same = not are_values_same

        # Return 0 if the flag indicates that the values are the same; otherwise, return 1.
        return 0 if are_values_same else 1