package main

import (
	"fmt"
	"time"
)

func client(name string, toServer chan chan string, done chan<- bool) {
    responseChannel := make(chan string)
 
    toServer <- responseChannel
    responseChannel <- name
 
    fmt.Println(<-responseChannel)
 
    done <- true
}
 
func worker(clientChannel chan string) {
    name := <-clientChannel
    response := fmt.Sprintf("Worker: Hello %s", name)
 
    clientChannel <- response
}
 
func server(fromClient chan chan string, kill <-chan bool) {
    for {
        select {
            case responseChannel := <-fromClient:
                go worker(responseChannel)
            case <-kill:
                fmt.Println("Server: terminating.. BYE BYE")
                return
        }
    }
}
 
func main() {
    const max int = 5
    toServer := make(chan chan string)
    killServer := make(chan bool)
    done := make(chan bool)
 
    go server(toServer, killServer)
 
    for i := 0; i < max; i++ {
        name := fmt.Sprintf("%d", i)
        go client(name, toServer, done)
    }
 
    for i := 0; i < max; i++ {
        <-done
    }
 
    killServer <- true
    time.Sleep(time.Second)
}