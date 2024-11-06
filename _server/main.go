package main

import (
	"context"
	"fmt"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/ollama/ollama/api"
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

var hasStream bool = true

var client *api.Client

func init() {
	var err error
	client, err = api.ClientFromEnvironment()
	if err != nil {
		log.Fatal(err)
	}
}

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

func main() {
	router := gin.Default()
	router.Static("/static", "./static")

	router.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.html", nil)
	})

	router.POST("/generate", handleGenerate)

	// router.GET("/ws", func(c *gin.Context) {
	// 	handleWebSocket(c.Writer, c.Request)
	// })

	router.Run("0.0.0.0:8080")
}
