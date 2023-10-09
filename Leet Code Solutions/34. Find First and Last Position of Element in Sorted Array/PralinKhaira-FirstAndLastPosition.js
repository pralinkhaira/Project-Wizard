var searchRange = function(nums, target) {
    const findLeft = (nums, target) => {
        let left = 0;
        let right = nums.length - 1;
        let index = -1;

        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            if (nums[mid] === target) {
                index = mid;
                right = mid - 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return index;
    };

    const findRight = (nums, target) => {
        let left = 0;
        let right = nums.length - 1;
        let index = -1;

        while (left <= right) {
            let mid = Math.floor((left + right) / 2);
            if (nums[mid] === target) {
                index = mid;
                left = mid + 1;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return index;
    };

    const leftIndex = findLeft(nums, target);
    const rightIndex = findRight(nums, target);

    if (leftIndex <= rightIndex) {
        return [leftIndex, rightIndex];
    } else {
        return [-1, -1];
    }
};