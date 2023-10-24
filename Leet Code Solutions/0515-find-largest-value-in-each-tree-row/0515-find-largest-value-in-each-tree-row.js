function largestValues(root) {
    if (!root) return [];
    
    const result = [];
    const queue = [root];
    
    while (queue.length) {
        let curr_level_size = queue.length;
        let max_val = Number.MIN_SAFE_INTEGER;
        
        for (let i = 0; i < curr_level_size; i++) {
            const node = queue.shift();
            max_val = Math.max(max_val, node.val);
            
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        
        result.push(max_val);
    }
    
    return result;
}