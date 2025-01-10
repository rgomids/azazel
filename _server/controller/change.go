package controller

import (
	"azazel/database"
	"azazel/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func HandleConfigUpdate(c *gin.Context) {
	var configs models.Configs

	if err := c.ShouldBind(&configs); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	if err := configs.UpdateConfig(database.DB); err != nil {
		status := http.StatusInternalServerError
		if err.Error() == "config not found" {
			status = http.StatusNotFound
		}
		c.JSON(status, gin.H{
			"error": err.Error(),
		})
		return
	}

	response := gin.H{
		"response":   "Ok",
		"ID":         configs.ID,
		"ConfigName": configs.ConfigName,
		"Value":      configs.Value,
	}

	c.JSON(http.StatusOK, response)

}
