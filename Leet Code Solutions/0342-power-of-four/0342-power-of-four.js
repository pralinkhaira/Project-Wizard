/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    if (n <= 0) return false;
    const x = Math.log(n) / Math.log(4);
    return Number.isInteger(x);
};