use std::thread;
use std::time::Duration;

extern crate thread_pool;
use thread_pool::ThreadPool;


fn main() {
    let pool = ThreadPool::new(5);

    loop{
        pool.execute(|| {
            letscount();
        });

        pool.execute(|| {
            println!("testing return values: {}", add(3.9, 5.4));
        });
        
        pool.execute(|| {
            wait();
        });
    }
}

fn letscount() {
    println!("testing console from within worker");
    for i in 1..4 {
        println!("test {}", i);
    }
}

fn add(a: f64, b: f64) -> f64 {
    let sum = a + b;

    sum
}

fn wait() {
    println!("testing wait");
    thread::sleep(Duration::from_secs(4));
    println!("wait done!");
}
