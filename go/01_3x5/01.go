package main

import "fmt"

func main() {
	fmt.Print(multsum35(10))
}

func multsum35(max int) int {
	sum := 0
	for i := 0; i < max; i++ {

		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	return sumpackage main

	import "fmt"
	
	func main() {
		fmt.Print(multsum35(10))
	}
	
	func multsum35(max int) int {
		sum := 0
		for i := 0; i < max; i++ {
	
			if i%3 == 0 || i%5 == 0 {
				sum += i
			}
		}
		return sum
	}
	
