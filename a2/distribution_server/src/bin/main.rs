use std::thread;
use std::time::Duration;

extern crate distribution_server;
use distribution_server::ThreadPool;

use std::io::prelude::*;
use std::net::TcpStream;
use std::net::TcpListener;
use std::fs;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

   // for stream in listener.incoming() {
   //     let stream = stream.unwrap();
    loop{
        pool.execute(|| {
        letscount();
        //handle_connection(stream);
    });
    }
    
    //}
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 512];
    stream.read(&mut buffer).unwrap();

    let get = b"GET / HTTP/1.1\r\n";

    if buffer.starts_with(get) {
        let contents = fs::read_to_string("hello.html").unwrap();

        let response = format!("HTTP/1.1 200 OK\r\n\r\n{}", contents);

        stream.write(response.as_bytes()).unwrap();
        stream.flush().unwrap();
    } else {
        let status_line = "HTTP/1.1 404 NOT FOUND\r\n\r\n";
        let contents = fs::read_to_string("404.html").unwrap();

        let response = format!("{}{}", status_line, contents);

        stream.write(response.as_bytes()).unwrap();
        stream.flush().unwrap();
    }
}



fn letscount() {
    
    //loop {
    //}
    for i in 1..10 {
        println!("test {}", i);
      //  thread::sleep(Duration::from_millis(1));
    }
}
/*
fn main() {
    /*
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
    */

    let threadpool = ThreadPool::new(4);

    threadpool.execute(|| {
        letscount();
    });
    //handle.join().unwrap();
} */
