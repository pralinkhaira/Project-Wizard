class Solution {
    function searchRange($nums, $target) {
        $leftIndex = $this->findLeft($nums, $target);
        $rightIndex = $this->findRight($nums, $target);

        if ($leftIndex <= $rightIndex) {
            return [$leftIndex, $rightIndex];
        } else {
            return [-1, -1];
        }
    }

    private function findLeft($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;
        $index = -1;

        while ($left <= $right) {
            $mid = $left + floor(($right - $left) / 2);
            if ($nums[$mid] == $target) {
                $index = $mid;
                $right = $mid - 1;
            } elseif ($nums[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }

        return $index;
    }

    private function findRight($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;
        $index = -1;

        while ($left <= $right) {
            $mid = $left + floor(($right - $left) / 2);
            if ($nums[$mid] == $target) {
                $index = $mid;
                $left = $mid + 1;
            } elseif ($nums[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }

        return $index;
    }
}