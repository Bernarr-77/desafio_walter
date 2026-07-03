package main

import (
	"fmt"
	"reflect"
)

func main() {
	lista := []any{67, "oi", 4.33, false, []int{1, 2}} // para criar a lista se usa: []tipo{valores da lista...}
	for i, item := range lista {                       // percorre toda a lista
		tipo := reflect.TypeOf(item)                               // puxa o metadado do item da vez
		fmt.Println(i, "Tipo do dado do item, ", item, ": ", tipo) // exibe
	}
}
