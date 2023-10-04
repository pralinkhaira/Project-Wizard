/*
Alien Dictionary
Problem Link: https://practice.geeksforgeeks.org/problems/alien-dictionary/1
*/

class Solution{
    public:
    string findOrder(string dict[], int N, int K) {
        //adjacency list
        vector<int>adj[K];
        //indegree vector
        vector<int>in(K,0);
        queue<int>q;
        string s="";
        //Creating an array of alphabets(0-indexed) just to map integer to its corresponding character
        int ch[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        for(int i=0;i<N-1;i++)
        {
            //selecting pair wise strings and creating an adjacency list of the first different character encountered
            string s1=dict[i];
            string s2=dict[i+1];
            for(int j=0;j<min(s1.size(),s2.size());j++)
            {
                if(s1[j]!=s2[j])
                {
                    adj[s1[j]-'a'].push_back(s2[j]-'a');
                    break;
                }
            }
        }
            for(int i=0;i<K;i++)
            {
                for(auto j:adj[i])
                {
                    in[j]++;
                }
            }
            for(int i=0;i<K;i++)
            {
                if(in[i]==0)
                q.push(i);
            }
            while(!q.empty())
            {
                int f=q.front();
                q.pop();
                //ch[f] returns the corresponding character and appends it to string s
                s+=ch[f];
                for(auto i:adj[f])
                {
                    in[i]--;
                    if(in[i]==0)
                    q.push(i);
                }
            }
        
        return s;
    }
};

