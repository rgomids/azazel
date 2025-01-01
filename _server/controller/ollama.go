package controller

import (
	"azazel/models"
	"context"
	"fmt"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/ollama/ollama/api"
)

var hasStream bool = true

var client *api.Client

func init() {
	var client_err error
	client, client_err = api.ClientFromEnvironment()
	if client_err != nil {
		log.Fatal(client_err)
	}

}

func ServeGenerate(c *gin.Context) {
	var msg models.Message
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
