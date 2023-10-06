/*
Problem Link: https://practice.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1
*/
class Solution
{
public:
    Node* pairWiseSwap(struct Node* head)
    {
        // If the list is empty or has only one node, no swapping is needed
        if (head == NULL || head->next == NULL)
            return head;

        // Initialize three pointers: prev, curr, and next
        Node* prev = NULL;
        Node* curr = head;
        Node* next = head->next;

        // Update the new head of the modified list
        head = next;

        // Traverse the list and swap pairs of nodes
        while (next != NULL)
        {
            // Adjust pointers to swap nodes
            curr->next = next->next;
            next->next = curr;

            // Update prev if it's not NULL
            if (prev != NULL)
                prev->next = next;

            // Move pointers to the next pair of nodes
            prev = curr;
            curr = curr->next;

            // Check if there's a pair to swap
            if (curr != NULL)
                next = curr->next;
            else
                next = NULL;
        }

        return head;
    }
};
