package main

import "fmt"

func main() {
	var lado1 int
	var lado2 int
	var lado3 int
	fmt.Print("Digite o primeiro lado: ")
	fmt.Scan(&lado1)
	fmt.Print("Digite o segundo lado: ")
	fmt.Scan(&lado2)
	fmt.Print("Digite o terceiro lado: ")
	fmt.Scan(&lado3)
	if lado1 == lado2 && lado2 == lado3 {
		fmt.Println("É um triangulo equilátero")
	} else if lado1 == lado2 || lado2 == lado3 || lado1 == lado3 {
		fmt.Println("É um triangulo isósceles")
	} else {
		fmt.Println("É um triangulo escaleno")
	}
}
