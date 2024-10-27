use yijia_ids706_mini_proj8::stats::{mean, median};
use std::time::Instant;
use sysinfo::{System, SystemExt};

#[test]
fn test_mean_performance() {
    let numbers = vec![1.0; 10_000_000]; // Use 10 million elements

    // Initialize the system for memory tracking
    let mut sys = System::new_all();
    sys.refresh_memory();
    let memory_before = sys.used_memory();

    let start = Instant::now();
    mean(&numbers);
    let duration = start.elapsed();

    // Capture memory after execution
    sys.refresh_memory();
    let memory_after = sys.used_memory();

    println!("Rust - Time taken for mean calculation: {:?}", duration);
    println!(
        "Rust - Memory usage for mean calculation: {} KB",
        memory_after as i64 - memory_before as i64
    );
}

#[test]
fn test_median_performance() {
    let mut numbers = vec![1.0; 10_000_000]; // Use 10 million elements

    // Initialize the system for memory tracking
    let mut sys = System::new_all();
    sys.refresh_memory();
    let memory_before = sys.used_memory();

    let start = Instant::now();
    median(&mut numbers);
    let duration = start.elapsed();

    // Capture memory after execution
    sys.refresh_memory();
    let memory_after = sys.used_memory();

    println!("Rust - Time taken for median calculation: {:?}", duration);
    println!(
        "Rust - Memory usage for median calculation: {} KB",
        memory_after as i64 - memory_before as i64
    );
}