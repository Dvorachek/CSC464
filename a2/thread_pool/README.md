# Part 3: Custom Threadpool library for rust

This implementation of a threadpool library will be used by the main thread to distribute work to the worker CPUs (working on an n-body simulator with Neal Manning). Here the worker threads will be modified further to be given various attributes representative of CPU performance once we decide on a structure.

src/lib.rs contains the code for the thread_pool library.

src/bin/main.rs is used to demonstrate the library's usage.


