impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
        if n <= 0 {
        return false;
    }
    
    let x = (n as f64).log(4.0);
    (x % 1.0).abs() < f64::EPSILON
    }
}