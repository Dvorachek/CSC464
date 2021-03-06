# Part 3: Custom Threadpool library for rust

This implementation of a threadpool library will be used by the main thread to distribute work to the worker CPUs (working on an n-body simulator with Neal Manning). Here the worker threads could be modified further to be given various attributes representative of CPU performance once we decide on a structure.

src/lib.rs contains the code for the thread_pool library.

src/main.rs is used to demonstrate the library's usage.

Main loops through three different functions. One function tests return values, another tests stdout, and the last uses a sleep to demonstrate each of the threads gets used within the loop.

To execute code `cargo run`

### Sample output from main.rs:
    Worker 0 got job, executing
    testing console from within worker
    test 1
    test 2
    test 3
    Worker 0 got job, executing
    testing wait
    Worker 3 got job, executing
    testing console from within worker
    test 1
    test 2
    test 3
    Worker 1 got job, executing
    testing return values: 9.3
    Worker 4 got job, executing
    testing return values: 9.3
    Worker 2 got job, executing
    testing wait
    Worker 3 got job, executing
    testing console from within worker
    test 1
    test 2
    test 3
    Worker 4 got job, executing
    testing wait
    Worker 3 got job, executing
    testing console from within worker
    test 1
    test 2
    test 3
    Worker 1 got job, executing
    testing return values: 9.3
    Worker 1 got job, executing
    testing wait
    Worker 3 got job, executing
    testing return values: 9.3
    Worker 3 got job, executing
    testing console from within worker
    test 1
    test 2
    test 3
    Worker 3 got job, executing
    testing return values: 9.3
    Worker 3 got job, executing
    testing wait
    wait done!
    wait done!
