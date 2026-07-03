package main

import (
	"fmt"
	"math"
)

func main() {
	var velocidade float64
	var massa float64
	fmt.Print("Digite a velocidade: ")
	fmt.Scan(&velocidade)
	fmt.Print("Digite a massa: ")
	fmt.Scan(&massa)
	metros := velocidade / 3.6
	fmt.Println("Sua velocidade em m/s: ", metros)
	cinetica := math.Pow(metros, 2)
	valor := (massa * cinetica) / 2
	fmt.Println("Sua energia cinetica: ", valor)
}
