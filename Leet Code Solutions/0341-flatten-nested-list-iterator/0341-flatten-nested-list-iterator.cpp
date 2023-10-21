class NestedIterator {
private:
    // The list of NestedInteger elements to be flattened
    vector<NestedInteger> nestedList;

    // The flattened list of integers
    vector<int> flattenedList;

    // Index to keep track of the current position in the flattenedList
    int currentIndex = 0;

    // Recursively flattens the nested list and adds integers to the flattenedList
    void flatten(vector<NestedInteger>& currentList) {
        for (int i = 0; i < currentList.size(); i++) {
            if (currentList[i].isInteger()) {
                flattenedList.push_back(currentList[i].getInteger());
            } else {
                // Recursively flatten nested lists
                flatten(currentList[i].getList());
            }
        }
    }

public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        this->nestedList = nestedList;
        // Flatten the nestedList during initialization
        flatten(nestedList);
    }

    // Returns the next integer in the flattened list
    int next() {
        int number = flattenedList[currentIndex];
        currentIndex++;
        return number;
    }

    // Checks if there are more integers in the flattened list
    bool hasNext() {
        return currentIndex < flattenedList.size();
    }
};