class Solution {

function numFactoredBinaryTrees($arr) {
    sort($arr);
    $s = array_flip($arr);
    $dp = [];
    foreach ($arr as $x) $dp[$x] = 1;
    
    foreach ($arr as $i) {
        foreach ($arr as $j) {
            if ($j > sqrt($i)) break;
            if ($i % $j == 0 && isset($s[$i / $j])) {
                $temp = (int)((($dp[$j] * $dp[$i / $j]) % 1000000007) * ($i / $j == $j ? 1 : 2));
                $dp[$i] = ($dp[$i] + $temp) % 1000000007;
            }
        }
    }
    
    return array_sum($dp) % 1000000007;
}
}