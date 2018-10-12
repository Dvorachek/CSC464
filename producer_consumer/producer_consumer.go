package main

import (
	"fmt"
	"time"
)

func producer(talk chan bool, done chan bool) {
	for i := 0; i < 1000000; i++ {
		talk <- true
	}
	done <- true
}

func consumer(killCon chan bool, talk chan bool) {
	magicNumber := 0
	for {
		select {
		case <-killCon:
			fmt.Printf("Magic Number = %d", magicNumber)
			return
		case <-talk:
			magicNumber++
		}
	}
}

func main() {
	start := time.Now()
	killCon := make(chan bool)
	talk := make(chan bool)
	done := make(chan bool)
	go producer(talk, done)
	go consumer(killCon, talk)
	<-done
	killCon <- true
	fmt.Printf("\nRuntime = %s", time.Since(start))
}
