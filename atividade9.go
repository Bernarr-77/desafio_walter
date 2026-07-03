package main

import (
	"fmt"
	"math"
)

func main() {
	pi := 3.14159
	var raio float64
	fmt.Print("Digite o raio: ")
	fmt.Scan(&raio)
	area := pi * math.Pow(raio, 2)
	fmt.Println("O raio da base é´: ", area)

}
