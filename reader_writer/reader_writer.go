package main

import (
	"fmt"
	"time"
)

func reader(read chan chan int) {
	currentVal := make(chan int)
	read <- currentVal
	fmt.Println("Reader: count = ", <-currentVal)
}

func writer(n int, add chan int) {
	add <- n
}

func countResource(read chan chan int, add chan int, kill chan bool) {
	count := 0

	for {
		select {
		case x := <-add:
			count = count + x
			fmt.Println("Monitor: updating count to ", count)
		case readRequest := <-read:
			readRequest <- count
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

	go countResource(read, add, kill)

	writer(10, add)
	reader(read)

	kill <- true
	time.Sleep(time.Second)
}
