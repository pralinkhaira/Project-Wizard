// Problem link: https://practice.geeksforgeeks.org/problems/eventual-safe-states/1

// User function Template for Java

class Solution {

      List<Integer> eventualSafeNodes(int V, List<List<Integer>> adj) {    
        List<List<Integer>> revAdj = new ArrayList<>();
        int[] inDegree = new int[V];
        for(int i = 0; i < V; i++) revAdj.add(new ArrayList<>());
        
        for(int i = 0; i < V; i++) {
            for(int node: adj.get(i)) {
                revAdj.get(node).add(i);
                inDegree[i]++;
            }
        }
        
        Queue<Integer> q = new LinkedList<>();
        List<Integer> list = new ArrayList<>();
        
        for(int i = 0; i < V; i++) if(inDegree[i] == 0) q.add(i);
        
        while(q.size() > 0) {
            int curr = q.remove();
            list.add(curr);
            for(int nbr: revAdj.get(curr)) {
                inDegree[nbr]--;
                if(inDegree[nbr] == 0) q.add(nbr);
            }
        }
        Collections.sort(list);
        return list;
    }
}
