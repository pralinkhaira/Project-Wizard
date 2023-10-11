var fullBloomFlowers = function(flowers, persons) {
    const heap = new MinPriorityQueue({compare: (a, b) => a[1] - b[1]});
    
    flowers.sort((a, b) => a[0] - b[0]);
    
    const sortedPersons = persons.slice().sort((a, b) => a - b);
    
    const map = {};
    
    let i = 0;
    
    for (const person of sortedPersons) {
      while (i < flowers.length && flowers[i][0] <= person) {
        heap.enqueue(flowers[i]);
        ++i;      
      }
  
      while (heap.size() && heap.front()[1] < person) {
        heap.dequeue();
      }
      
      map[person] = heap.size();
    }
    
    return persons.map(person => map[person]);
  };