use yijia_ids706_mini_proj8::stats::{mean, median};
use std::time::Instant;

fn main() {
    // Performance test for mean
    let numbers = vec![1.0; 1_000_000];
    let start = Instant::now();
    mean(&numbers);
    let duration = start.elapsed();
    println!("Rust - Time taken for mean calculation: {:?}", duration);

    // Performance test for median
    let mut numbers = vec![1.0; 1_000_000];
    let start = Instant::now();
    median(&mut numbers);
    let duration = start.elapsed();
    println!("Rust - Time taken for median calculation: {:?}", duration);
}
