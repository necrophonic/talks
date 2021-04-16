package main

import (
	"fmt"
	"time"
)

// Greet returns a nice greeting including
// the current date and time
func Greet() string {
	return "Hello! The time is " + now()
}

func now() string {
	return time.Now().Format(time.RFC3339)
}

func main() {
	fmt.Println(Greet())
}
