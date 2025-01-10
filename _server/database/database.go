package database

import (
	"azazel/models"
	"log"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

const (
	dbPath     = "azazel.db"
	llmColumn  = "llm_model"
	defaultLlm = "ollama"
)

var (
	DB  *gorm.DB
	err error
)

func SolveDatabase() {
	DB, err = gorm.Open(sqlite.Open(dbPath))
	if err != nil {
		log.Panic("Erro ao conectar com banco de dados")
	}
	DB.AutoMigrate(&models.Configs{})
	DB.FirstOrCreate(&models.Configs{ConfigName: llmColumn}, &models.Configs{Value: defaultLlm})
}
