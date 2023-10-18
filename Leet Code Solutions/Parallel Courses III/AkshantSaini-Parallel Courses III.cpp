//2050. Parallel Courses III
//Problem Link: https://leetcode.com/problems/parallel-courses-iii/description/
    // Approach: Dynamic Programming with Memoization
    // We represent the course prerequisites as a graph.
    // We use memoization to avoid redundant calculations when calculating the time needed for each course.
    // The recursive function 'calculateTime' calculates the time needed for a course, considering its prerequisites.
    // The overall minimum time is obtained by iterating through all courses and finding the maximum time needed.

class Solution {
public:
   
    int minimumTime(int n, const std::vector<std::vector<int>>& relations, const std::vector<int>& time) {
        // Create a graph to represent the prerequisites
        std::vector<std::vector<int>> graph(n);

        // Build the graph based on the given relations
        for (const auto& relation : relations) {
            int prev = relation[0] - 1;
            int next = relation[1] - 1;
            graph[prev].push_back(next);
        }

        // Memoization array to store calculated times for each course
        std::vector<int> memo(n, -1);

        // Recursive function to calculate time needed for a course
        std::function<int(int)> calculateTime = [&](int course) -> int {
            // If time for this course is already calculated, return it
            if (memo[course] != -1) {
                return memo[course];
            }

            // If the course has no prerequisites, its time is simply its own time
            if (graph[course].empty()) {
                memo[course] = time[course];
            } else {
                // Calculate the maximum time among its prerequisites
                int maxPrerequisiteTime = 0;
                for (int prereq : graph[course]) {
                    maxPrerequisiteTime = std::max(maxPrerequisiteTime, calculateTime(prereq));
                }

                // The time for the current course is the maximum time among prerequisites plus its own time
                memo[course] = maxPrerequisiteTime + time[course];
            }

            return memo[course];
        };

        // Variable to store the overall minimum time
        int overallMinTime = 0;

        // Calculate the overall minimum time needed to complete all courses
        for (int course = 0; course < n; course++) {
            overallMinTime = std::max(overallMinTime, calculateTime(course));
        }

        return overallMinTime;
    }
};
