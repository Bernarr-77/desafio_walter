package main

import "fmt"

func main() {
	var numeroUser int
	fmt.Print("Digite um numero: ")
	fmt.Scan(&numeroUser)
	for i := numeroUser; i <= 100; i += numeroUser {
		fmt.Println("Numero: ", i)
	}
}
