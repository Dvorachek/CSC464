package main

import (
	"fmt"
	"time"
)

func reader(read chan chan int) {
	current_val := make(chan int)
	read <- current_val
	fmt.Println("Reader: count = ", <-current_val)
}

func writer(n int, add chan int) {
	add <- n
}

func count_resource(read chan chan int, add chan int, kill chan bool) {
	count := 0

	for {
		select {
		case x := <-add:
			count = count + x
			fmt.Println("Monitor: updating count to ", count)
		case read_request := <-read:
			read_request <- count
		case <-kill:
			fmt.Println("Monitor: terminating.. BYE BYE")
			return
		}
	}
}

func main() {
	read := make(chan chan int)
	add := make(chan int)
	kill := make(chan bool)

	go count_resource(read, add, kill)

	writer(10, add)
	reader(read)

	kill <- true
	time.Sleep(time.Second)
}
