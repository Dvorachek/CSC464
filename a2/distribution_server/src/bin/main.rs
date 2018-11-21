use std::thread;
use std::time::Duration;

extern crate distribution_server;
use distribution_server::ThreadPool;

fn main() {

    let vector = vec![1, 2, 3];

    thread::spawn( move || {
        println!("vector = {:?}", vector);
    });

    let handle = thread::spawn(|| {
        for i in 1..2 {
            println!("thread number {} from the thread spawn", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..2 {
        println!("number {} from the main thread", i);
        thread::sleep(Duration::from_millis(2));
    }


    //handle.join().unwrap();
}
