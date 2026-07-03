package main

import "fmt"

func main() {
	var base float64
	var altura float64
	fmt.Print("Digite a base: ")
	fmt.Scan(&base)
	fmt.Print("Digite a altura: ")
	fmt.Scan(&altura)
	area := (base * altura) / 2
	fmt.Println(area)
}
