class Solution {
    function maximumScore($nums, $k) {
        $left = $k;
        $right = $k;
        $min_val = $nums[$k];
        $max_score = $min_val;

        while ($left > 0 || $right < count($nums) - 1) {
            if ($left == 0 || ($right < count($nums) - 1 && $nums[$right + 1] > $nums[$left - 1])) {
                $right++;
            } else {
                $left--;
            }
            $min_val = min($min_val, min($nums[$left], $nums[$right]));
            $max_score = max($max_score, $min_val * ($right - $left + 1));
        }
        
        return $max_score;
    }
}