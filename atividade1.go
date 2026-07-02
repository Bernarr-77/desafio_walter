package main

import "fmt"

func main() {
	var idade int
	fmt.Print("Qual a sua idade? ")
	fmt.Scan(&idade) // salva o resultado da resposta na variavel
	if idade > 18 {  // if e else normal
		fmt.Println("MAior de idade")
	} else {
		fmt.Println("Menor de idade")
	}
}
