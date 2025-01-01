package main

import (
	"azazel/database"
	"azazel/route"
)

func main() {
	database.SolveDatabase()
	route.ServeRoutes()
}
