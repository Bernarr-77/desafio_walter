package main

import "fmt"

func main() {
	var celsius float64
	fmt.Print("Digite a temperatura: ")
	fmt.Scan(&celsius)
	Fahrenheit := (celsius * 1.8) + 32
	fmt.Println(Fahrenheit)
}
