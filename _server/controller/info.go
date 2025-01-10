package controller

import (
	"azazel/database"
	"azazel/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

var ImplementedLLMs = []string{"Ollama Server", "GPT-4"}

func HandleConfigList(c *gin.Context) {
	var configs models.Configs

	configNames, err := configs.ListConfigNames(database.DB)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"Response": "Ok",
		"Fields":   configNames,
	})
}

func HandleServices(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"response": "OK",
		"LLM's":    ImplementedLLMs,
	})
}
