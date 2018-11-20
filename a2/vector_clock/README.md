# Part 1: Vector Clocks

My implementation of vector clocks in Python involves the use of a class which contains a dictionary, representing an individual process’ clock. The implementation is fairly basic and non-concurrent which made testing considerably easier.

The vector clock class has methods for communicating with other vector clocks, doing arbitrary work, and to print the contents of its own clock.

There are two functions which test various operations between several vector clocks and then call another function which dumps the results to console. These tests require the final state of each vector clock to be evaluated, which provide another argument for keeping the implementation fairly simple.

The most important aspect of the vector clock is that each process has an up-to-date version of its own clock. This information can then be used to determine the order of last interactions each process had with each other, possibly demonstrating dependences. While I have not explicitly written tests to evaluate the ordering of these processes, by inspecting the console dumps it is easy to deduce provided the example is simple.

