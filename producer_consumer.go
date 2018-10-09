package main

import (
	"fmt"
	"time"
)

func producer(max int, talk chan string) {
	for i := 0; i < max; i++ {
		message := fmt.Sprintf("%d", i)
		talk <- message
		time.Sleep(time.Second)
	}
}

func consumer(killCon chan bool, talk chan string) {
	for {
		select {
		case <-killCon:
			fmt.Println("good bye")
			return
		case message := <-talk:
			fmt.Println(message)
		}
	}
}

func main() {
	killCon := make(chan bool)
	talk := make(chan string)

	go producer(10, talk)
	go producer(10, talk)
	go producer(10, talk)

	go consumer(killCon, talk)

	time.Sleep(time.Second * 8)
	killCon <- true
	time.Sleep(time.Second)

}
