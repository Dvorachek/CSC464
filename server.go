package main

import (
	"fmt"
	"time"
)

func client(name string, to_server chan chan string, done chan<- bool) {
    response_channel := make(chan string)
 
    to_server <- response_channel
    response_channel <- name
 
    fmt.Println(<-response_channel)
 
    done <- true
}
 
func worker(client_channel chan string) {
    name := <-client_channel
    response := fmt.Sprintf("Worker: Hello %s", name)
 
    client_channel <- response
}
 
func server(from_client chan chan string, kill <-chan bool) {
    for {
        select {
            case response_channel := <-from_client:
                go worker(response_channel)
            case <-kill:
                fmt.Println("Server: terminating.. BYE BYE")
                return
        }
    }
}
 
func main() {
    const max int = 5
    to_server := make(chan chan string)
    kill_server := make(chan bool)
    done := make(chan bool)
 
    go server(to_server, kill_server)
 
    for i := 0; i < max; i++ {
        name := fmt.Sprintf("%d", i)
        go client(name, to_server, done)
    }
 
    for i := 0; i < max; i++ {
        <-done
    }
 
    kill_server <- true
    time.Sleep(time.Second)
}