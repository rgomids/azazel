package database

import (
	consts "azazel/cmd"
	"azazel/models"
	"log"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

var (
	DB  *gorm.DB
	err error
)

func SolveDatabase() {
	DB, err = gorm.Open(sqlite.Open(consts.DBPath))
	if err != nil {
		log.Panic("Erro ao conectar com banco de dados")
	}
	DB.AutoMigrate(&models.Configs{})
	DB.FirstOrCreate(&models.Configs{ConfigName: consts.LLMConfigColumn}, &models.Configs{Value: consts.DefaultLLM})
}
