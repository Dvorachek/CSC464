package main

import (
	"fmt"
	"math/rand"
	"time"
)

func agent(agent chan bool, tobacco chan bool, match chan bool, paper chan bool) {
	for {
		<-agent
		choice := rand.Intn(3)
		if choice == 0 {
			fmt.Println("Agent places tobacco and paper on the table.")
			match <- true
		} else if choice == 1 {
			fmt.Println("Agent places tobacco and a match on the table.")
			paper <- true
		} else {
			fmt.Println("Agent places a match and paper on the table.")
			tobacco <- true
		}

		time.Sleep(time.Second)
	}
}

func smokerTobacco(agent chan bool, tobacco chan bool) {
	for {
		<-tobacco
		fmt.Println("Tobacco smoker picks up the paper and match.")
		agent <- true
	}
}

func smokerMatch(agent chan bool, match chan bool) {
	for {
		<-match
		fmt.Println("Match smoker picks up the tobacco and paper.")
		agent <- true
	}
}

func smokerPaper(agent chan bool, paper chan bool) {
	for {
		<-paper
		fmt.Println("Paper smoker picks up the tobacco and match.")
		agent <- true
	}
}

func main() {
	agentWake := make(chan bool)
	tobacco := make(chan bool)
	match := make(chan bool)
	paper := make(chan bool)

	go smokerTobacco(agentWake, tobacco)
	go smokerMatch(agentWake, match)
	go smokerPaper(agentWake, paper)
	go agent(agentWake, tobacco, match, paper)

	agentWake <- true

	time.Sleep(time.Second * 20)
}
