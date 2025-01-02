package controller

import (
	"azazel/database"
	"azazel/models"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

func ServeInfo(c *gin.Context) {

	var configNames []string
	if err := database.DB.Model(&models.Configs{}).Pluck("config_name", &configNames).Error; err != nil {
		log.Fatalf("Erro ao buscar os nomes das configurações: %v", err)
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"Fields": configNames,
	})
}
