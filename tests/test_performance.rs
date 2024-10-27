use std::fs::OpenOptions;
use std::io::Write;
use std::time::Instant;
use sysinfo::{System, SystemExt};
use yijia_ids706_mini_proj8::stats::{mean, median};

fn write_to_md(content: &str) {
    let mut file = OpenOptions::new()
        .create(true)
        .write(true)
        .append(true)
        .open("rust_performance.md")
        .expect("Unable to open rust_performance.md");
    writeln!(file, "{}", content).expect("Unable to write data");
}

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
    let memory_used = memory_after as i64 - memory_before as i64;

    let mean_report = format!(
        "### Mean Calculation Performance\n\n\
        - Time taken: {:?}\n\
        - Initial memory usage: {} KB\n\
        - Final memory usage: {} KB\n\
        - Memory consumed: {} KB\n\n",
        duration, memory_before, memory_after, memory_used
    );
    write_to_md(&mean_report);

    println!("Rust - Time taken for mean calculation: {:?}", duration);
    println!(
        "Rust - Memory usage for mean calculation: {} KB",
        memory_used
    );
}

#[test]
fn test_median_performance() {
    let mut numbers = vec![1.0; 10_000_000];

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
    let memory_used = memory_after as i64 - memory_before as i64;

    let median_report = format!(
        "### Median Calculation Performance\n\n\
        - Time taken: {:?}\n\
        - Initial memory usage: {} KB\n\
        - Final memory usage: {} KB\n\
        - Memory consumed: {} KB\n\n",
        duration, memory_before, memory_after, memory_used
    );
    write_to_md(&median_report);

    println!("Rust - Time taken for median calculation: {:?}", duration);
    println!(
        "Rust - Memory usage for median calculation: {} KB",
        memory_used
    );
}
