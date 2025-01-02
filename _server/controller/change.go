package controller

import (
	"azazel/database"
	"azazel/models"
	"net/http"

	"github.com/gin-gonic/gin"
)

func ServePatch(c *gin.Context) {
	var configs models.Configs

	if err := c.ShouldBind(&configs); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": err.Error(),
		})
		return
	}

	database.DB.Where(&models.Configs{ConfigName: configs.ConfigName}).First(&configs)

	if configs.ID == 0 {
		c.JSON(http.StatusNotFound, gin.H{
			"error": "Config not found!",
		})
		return
	}
	database.DB.Model(&configs).UpdateColumns(configs)
	c.JSON(http.StatusOK, configs)

}
