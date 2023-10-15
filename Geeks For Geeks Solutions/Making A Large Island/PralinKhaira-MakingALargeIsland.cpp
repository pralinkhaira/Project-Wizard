/*
Problem link: https://practice.geeksforgeeks.org/problems/making-a-large-island/1
*/

//User function Template for C++

class D{
public:
    vector<int> arr1, parent, size;
    D(int n) {
        arr1.resize(n + 1, 0);
        parent.resize(n + 1);
        size.resize(n + 1);
        for (int i = 0; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int findUPar(int node) {
        if (node == parent[node])
            return node;
        return parent[node] = findUPar(parent[node]);
    }

    void unionByRank(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (arr1[ulp_u] < arr1[ulp_v]) {
            parent[ulp_u] = ulp_v;
        }
        else if (arr1[ulp_v] < arr1[ulp_u]) {
            parent[ulp_v] = ulp_u;
        }
        else {
            parent[ulp_v] = ulp_u;
            arr1[ulp_u]++;
        }
    }

    void unionBySize(int u, int v) {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v) return;
        if (size[ulp_u] < size[ulp_v]) {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }
        else {
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
};
class Solution {
private:
    bool isValid(int a, int b, int n) {
        return a >= 0 && a < n && b >= 0 && b < n;
    }
public:
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size();
        D ds(n * n);
        for (int row = 0; row < n ; row++) {
            for (int col = 0; col < n ; col++) {
                if (grid[row][col] == 0) continue;
                int dr[] = { -1, 0, 1, 0};
                int dc[] = {0, -1, 0, 1};
                for (int ind = 0; ind < 4; ind++) {
                    int a = row + dr[ind];
                    int b = col + dc[ind];
                    if (isValid(a, b, n) && grid[a][b] == 1) {
                        int nodeNo = row * n + col;
                        int adjNodeNo = a * n + b;
                        ds.unionBySize(nodeNo, adjNodeNo);
                    }
                }
            }
        }
        int mx = 0;
        for (int row = 0; row < n; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == 1) continue;
                int dr[] = { -1, 0, 1, 0};
                int dc[] = {0, -1, 0, 1};
                set<int> components;
                for (int ind = 0; ind < 4; ind++) {
                    int a = row + dr[ind];
                    int b = col + dc[ind];
                    if (isValid(a, b, n)) {
                        if (grid[a][b] == 1) {
                            components.insert(ds.findUPar(a * n + b));
                        }
                    }
                }
                int sizeTotal = 0;
                for (auto it : components) {
                    sizeTotal += ds.size[it];
                }
                mx = max(mx, sizeTotal + 1);
            }
        }
        for (int cellNo = 0; cellNo < n * n; cellNo++) {
            mx = max(mx, ds.size[ds.findUPar(cellNo)]);
        }
        return mx;
    }
   };
