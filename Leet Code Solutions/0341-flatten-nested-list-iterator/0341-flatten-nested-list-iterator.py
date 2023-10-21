class NestedIterator:
    def __init__(self, nestedList):
        # The list of NestedInteger elements to be flattened
        self.nestedList = nestedList
        
        # The flattened list of integers
        self.flattenedList = []
        
        # Index to keep track of the current position in the flattenedList
        self.currentIndex = 0

        # Recursively flattens the nested list and adds integers to the flattenedList
        def flatten(currentList):
            for item in currentList:
                if item.isInteger():
                    self.flattenedList.append(item.getInteger())
                else:
                    # Recursively flatten nested lists
                    flatten(item.getList())
        
        # Flatten the nestedList during initialization
        flatten(self.nestedList)

    # Returns the next integer in the flattened list
    def next(self):
        number = self.flattenedList[self.currentIndex]
        self.currentIndex += 1
        return number

    # Checks if there are more integers in the flattened list
    def hasNext(self):
        return self.currentIndex < len(self.flattenedList)