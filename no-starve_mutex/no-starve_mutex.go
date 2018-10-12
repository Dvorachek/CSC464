package main

import (
	"fmt"
	"time"
)

func locks(checkMagicNumber chan bool, increment chan bool) {
	magicNumber := 0
	for {
		select {
		case <-increment:
			magicNumber++
		case <-checkMagicNumber:
			fmt.Printf("Iterations = %d", magicNumber)
			return
		}
	}
}

func noStarveThread(increment chan bool, done chan bool) {
	increment <- true
	done <- true
}

func main() {
	start := time.Now()

	const max int = 100000
	checkMagicNumber := make(chan bool)
	increment := make(chan bool)
	done := make(chan bool)

	go locks(checkMagicNumber, increment)

	for i := 0; i < max; i++ {
		go noStarveThread(increment, done)
	}

	for i := 0; i < max; i++ {
		<-done
	}

	checkMagicNumber <- true

	fmt.Printf("\nRuntime = %s\n", time.Since(start))
	time.Sleep(time.Second)
}
