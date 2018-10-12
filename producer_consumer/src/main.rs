// https://gist.github.com/krishnaIndia/f037882b11aca172e9f2

use std::sync::{Arc, Mutex, Condvar};
use std::thread;
use std::time::Instant;

struct Producer {
        cvar: Arc<(Mutex<bool>, Condvar)>
}

impl Producer {
    pub fn new(cvar: Arc<(Mutex<bool>, Condvar)>) -> Producer {
        Producer {
            cvar: cvar
        }
    }

    pub fn get_cvar(&self) ->  &Arc<(Mutex<bool>, Condvar)> {
        &self.cvar
    }

    pub fn start(&self) {
        let pair = self.cvar.clone();
        let start = Instant::now();
        thread::spawn(move || {
            for _ in 0..1000000 {
                let &(ref lock, ref cvar) = &*pair;
                //thread::sleep_ms(1000);
                let mut status = lock.lock().unwrap();
                *status = true;
                cvar.notify_all();
                *status = false;
            }
            
        });
        let end = Instant::now();
        println!("Runtime = {:?}", end.duration_since(start));
    }
}


struct Consumer<'a> {
    name: String,
    producer: &'a Producer
}

impl <'a>Consumer<'a> {
    pub fn new(name: String, producer: &'a Producer) -> Consumer<'a> {
        Consumer {
            name: name,
            producer: producer
        }
    }
    pub fn start(&self) {
        let prod = self.producer.get_cvar().clone();
        let name = self.name.clone();
        thread::spawn(move || {
                    let &(ref lock, ref cvar) = &*prod;
                    let mut fetched = lock.lock().unwrap();
                    loop {
                        fetched = cvar.wait(fetched).unwrap();
                        //println!("Recieved {}", name);
                    }
                });
    }
}


fn main() {
    let p = Producer::new(Arc::new((Mutex::new(false), Condvar::new())));
    let c = Consumer::new("c1".to_string(), &p);
    let c2 = Consumer::new("c2".to_string(), &p);
    p.start();
    c.start();
    c2.start();
    thread::sleep_ms(3000)
}