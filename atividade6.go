package main

import "fmt"

func main() {
	var num1 int
	var num2 int
	fmt.Print("Digite o primeiro numero: ")
	fmt.Scan(&num1)
	fmt.Print("Digite o segundo numero: ")
	fmt.Scan(&num2)
	if num1 > num2 {
		fmt.Println(num1, num2)
	} else {
		fmt.Println(num2, num1)
	}
}
