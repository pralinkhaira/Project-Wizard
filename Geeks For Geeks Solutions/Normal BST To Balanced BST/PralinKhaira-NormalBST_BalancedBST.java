// Problem Link: https://practice.geeksforgeeks.org/problems/normal-bst-to-balanced-bst/1

class GfG
{
    Node buildBalancedTree(Node root) 
    {
        //Add your code here.
        ArrayList<Integer> alist=new ArrayList<>();
        fill(root,alist);
        Collections.sort(alist);
        Node root1=build(alist,0,alist.size()-1);
        return root1;
        
    }
    public static Node build(ArrayList<Integer> alist,int l,int h)
    {
        int mid=(l+h)/2;
        if(l>h)
            return null;
        Node root=new Node(alist.get(mid));
        root.left=build(alist,l,mid-1);
        root.right=build(alist,mid+1,h);
        return root;
    }
    public static void  fill(Node root,ArrayList<Integer> alist)
    {
        if(root==null) return ;
        
        alist.add(root.data);
        fill(root.left,alist);
        fill(root.right,alist);
    }
    
}