/*
Problem Link: https://practice.geeksforgeeks.org/problems/insert-in-a-sorted-list/1
*/

/*
structure of the node of the list is as
struct Node
{
    int data;
    struct Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }
};
*/

class Solution{
  public:
    // Should return head of the modified linked list
    Node *sortedInsert(struct Node* head, int data) {
Node* newptr = new Node(data);
        if(head==NULL || head->data > data){
            newptr->next = head;
            head = newptr;
            return head;
        }
        Node* curr=head;
        while(curr->next!=NULL && curr->next->data<data){
            curr=curr->next;
        }
        newptr->next=curr->next;
        curr->next=newptr;                                                                      
        return head;
    }
};