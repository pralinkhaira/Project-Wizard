/*
Problem Link: https://practice.geeksforgeeks.org/problems/given-a-linked-list-reverse-alternate-nodes-and-append-at-the-end/1
*/


/*
  reverse alternate nodes and append at the end
  The input list will have at least one element  
  Node is defined as 
  struct Node
  {
      int data;
      struct Node *next;
    
      Node(int x){
        data = x;
        next = NULL;
      }
    
   };

*/
class Solution
{
    public:
    
    Node *reverse(Node *head){
        if(!head or !head->next) {
            return head;
        }
        
        Node *curr = head;
        Node *prev = NULL;
        while(curr!=NULL){
            Node *next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        
        return prev;
        
    }
    
    void rearrange(struct Node *odd)
    {
        //add code here
        Node*o = odd;
        Node*e = odd->next;
        Node*t = odd->next;
        while(o->next and e->next) {
            o->next = o->next->next;
            o = o->next;
            e->next = e->next->next;
            e = e->next;
        }
 
        // second = reverse(second);
        o->next = reverse(t);
    }
};
