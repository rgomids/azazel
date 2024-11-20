package main

import (
	"context"
	"fmt"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/ollama/ollama/api"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type GenerateRequest struct {
	Message string `json:"message"`
}

type GenerateResponse struct {
	Response string `json:"response"`
}

type Message struct {
	Content string `json:"content"`
}
type Configs struct {
	ID         uint   `gorm:"primaryKey"`
	ConfigName string `gorm:"size:50;not null;unique"`
	Value      string `gorm:"size:200;default:''"`
}

const (
	dbPath          = "azazel.db"
	LLMConfigColumn = "llm_model"
	DefaultLLM      = "ollama"
)

var hasStream bool = true

var client *api.Client

func callOllamaAPI(prompt string, respFunc api.GenerateResponseFunc) {

	req := &api.GenerateRequest{
		Model:  "llama3",
		Prompt: prompt,
		Stream: &hasStream,
	}

	ctx := context.Background()

	err := client.Generate(ctx, req, respFunc)
	if err != nil {
		log.Fatal(err)
	}

}

func handleGenerate(c *gin.Context) {
	var msg Message
	if err := c.BindJSON(&msg); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	var response string

	callOllamaAPI(msg.Content, func(resp api.GenerateResponse) error {
		response = fmt.Sprintf(`%s%v`, response, resp.Response)
		fmt.Print(resp.Response)
		return nil
	})

	c.JSON(http.StatusOK, gin.H{"responses": response})
}

func StartDB(db *gorm.DB) {
	if err := db.AutoMigrate(&Configs{}); err != nil {
		log.Fatalf("Erro ao migrar banco de dados: %v", err)
	}

	db.FirstOrCreate(&Configs{ConfigName: LLMConfigColumn}, &Configs{Value: DefaultLLM})
}

func init() {
	var client_err error
	client, client_err = api.ClientFromEnvironment()
	if client_err != nil {
		log.Fatal(client_err)
	}

	var db_err error
	db, db_err := gorm.Open(sqlite.Open(dbPath), &gorm.Config{})
	if db_err != nil {
		log.Fatalf("Erro ao conectar ao banco de dados: %v", db_err)
	}
	StartDB(db)

}

func main() {
	router := gin.Default()

	router.POST("/generate", handleGenerate)

	router.Run("0.0.0.0:8080")
}
