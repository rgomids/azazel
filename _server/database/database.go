package database

import (
	"azazel/models"
	"log"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

const (
	DBPath          = "azazel.db"
	LLMConfigColumn = "llm_model"
	DefaultLLM      = "ollama"
)

var (
	DB  *gorm.DB
	err error
)

func SolveDatabase() {
	DB, err = gorm.Open(sqlite.Open(DBPath))
	if err != nil {
		log.Panic("Erro ao conectar com banco de dados")
	}
	DB.AutoMigrate(&models.Configs{})
	DB.FirstOrCreate(&models.Configs{ConfigName: LLMConfigColumn}, &models.Configs{Value: DefaultLLM})
}
