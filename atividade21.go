package main

import (
	"fmt"
	"math"
)

func main() {
	var A float64
	var B float64
	fmt.Print("Digite o primeiro numero: ")
	fmt.Scan(&A)
	fmt.Print("Digite o segundo numero: ")
	fmt.Scan(&B)
	soma := A + B
	resultado := math.Pow(soma, 2)
	fmt.Println(resultado)
}
